from unittest.mock import AsyncMock, MagicMock

import pytest
from playwright.async_api import Error

from scrapers import playwright_scraper
from scrapers.playwright_scraper import PlaywrightScraper


def make_page(quotes=None, error=None):
    page = MagicMock()
    page.goto = AsyncMock(side_effect=error)
    page.evaluate = AsyncMock(return_value=quotes if quotes is not None else [])
    page.close = AsyncMock()
    return page


class FakePlaywrightManager:
    def __init__(self, browser):
        self.playwright = MagicMock()
        self.playwright.chromium.launch = AsyncMock(return_value=browser)

    async def __aenter__(self):
        return self.playwright

    async def __aexit__(self, *exc_info):
        return False


@pytest.fixture
def browser():
    instance = MagicMock()
    instance.new_context = AsyncMock(return_value=MagicMock())
    instance.close = AsyncMock()
    return instance


@pytest.fixture
def install_browser(monkeypatch, browser):
    monkeypatch.setattr(
        playwright_scraper,
        "async_playwright",
        lambda: FakePlaywrightManager(browser),
    )
    return browser


async def test_scrape_page_returns_extracted_quotes():
    quote = {"text": "Q", "author": "A", "tags": "t"}
    page = make_page(quotes=[quote])
    context = MagicMock()
    context.new_page = AsyncMock(return_value=page)

    result = await PlaywrightScraper()._scrape_page(context, "http://t/page/1/")

    assert result == [quote]
    page.goto.assert_awaited_once()
    page.close.assert_awaited_once()


async def test_scrape_page_returns_empty_list_on_playwright_error():
    page = make_page(error=Error("navigation failed"))
    context = MagicMock()
    context.new_page = AsyncMock(return_value=page)

    result = await PlaywrightScraper()._scrape_page(context, "http://t/page/1/")

    assert result == []
    page.close.assert_awaited_once()


async def test_scrape_quotes_async_combines_pages_in_order(install_browser):
    first = {"text": "One", "author": "A", "tags": ""}
    second = {"text": "Two", "author": "B", "tags": ""}
    context = await install_browser.new_context()
    context.new_page = AsyncMock(side_effect=[make_page([first]), make_page([second])])

    quotes = await PlaywrightScraper().scrape_quotes_async(base_url="http://t", max_pages=2)

    assert quotes == [first, second]
    install_browser.close.assert_awaited_once()


async def test_scrape_quotes_async_ignores_failed_pages(install_browser):
    quote = {"text": "Only", "author": "A", "tags": ""}
    context = await install_browser.new_context()
    context.new_page = AsyncMock(
        side_effect=[make_page(error=Error("timeout")), make_page([quote])],
    )

    quotes = await PlaywrightScraper().scrape_quotes_async(base_url="http://t", max_pages=2)

    assert quotes == [quote]
