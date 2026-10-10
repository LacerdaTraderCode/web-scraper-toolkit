from unittest.mock import MagicMock

import pytest
import requests
from bs4 import BeautifulSoup
from tenacity import wait_none

from scrapers import bs4_scraper
from scrapers.bs4_scraper import BeautifulSoupScraper

PAGE_ONE = """
<div class="quote">
  <span class="text">First quote</span>
  <small class="author">Author A</small>
  <div class="tags"><a class="tag">life</a><a class="tag">love</a></div>
</div>
<ul><li class="next"><a href="/page/2/">Next</a></li></ul>
"""

PAGE_TWO = """
<div class="quote">
  <span class="text">Second quote</span>
  <small class="author">Author B</small>
</div>
"""


def soup(html):
    return BeautifulSoup(html, "lxml")


@pytest.fixture
def scraper(monkeypatch):
    monkeypatch.setattr(bs4_scraper, "get_random_user_agent", lambda: "Test-Agent")
    instance = BeautifulSoupScraper()
    instance.rate_limiter = MagicMock()
    instance.session = MagicMock()
    return instance


@pytest.fixture(autouse=True)
def no_retry_delay(monkeypatch):
    monkeypatch.setattr(BeautifulSoupScraper.fetch.retry, "wait", wait_none())


def test_fetch_returns_parsed_html(scraper):
    scraper.session.get.return_value.text = PAGE_TWO

    result = scraper.fetch("https://example.com")

    assert result.find("span", class_="text").get_text() == "Second quote"
    scraper.rate_limiter.wait.assert_called_once_with()
    _, kwargs = scraper.session.get.call_args
    assert kwargs["headers"] == {"User-Agent": "Test-Agent"}


def test_fetch_retries_then_raises_http_error(scraper):
    scraper.session.get.return_value.raise_for_status.side_effect = requests.HTTPError("500")

    with pytest.raises(requests.HTTPError):
        scraper.fetch("https://example.com")

    assert scraper.session.get.call_count == 3


def test_scrape_quotes_follows_pagination(scraper, monkeypatch):
    pages = {"/page/1/": PAGE_ONE, "/page/2/": PAGE_TWO}
    monkeypatch.setattr(scraper, "fetch", lambda url: soup(pages[url.removeprefix("http://t")]))

    quotes = scraper.scrape_quotes(base_url="http://t")

    assert quotes == [
        {"text": "First quote", "author": "Author A", "tags": "life, love"},
        {"text": "Second quote", "author": "Author B", "tags": ""},
    ]


def test_scrape_quotes_stops_on_empty_page(scraper, monkeypatch):
    monkeypatch.setattr(scraper, "fetch", lambda url: soup("<html></html>"))

    assert scraper.scrape_quotes(base_url="http://t") == []


def test_close_closes_session(scraper):
    scraper.close()

    scraper.session.close.assert_called_once_with()
