from unittest.mock import MagicMock

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from scrapers import selenium_scraper
from scrapers.selenium_scraper import SeleniumScraper


def make_article(title="Book", price="£10.00", stock=" In stock ", rating="star-rating Three"):
    elements = {
        "star-rating": MagicMock(**{"get_attribute.return_value": rating}),
        "h3 a": MagicMock(**{"get_attribute.return_value": title}),
        "price_color": MagicMock(text=price),
        "availability": MagicMock(text=stock),
    }
    article = MagicMock()
    article.find_element.side_effect = lambda by, value: elements[value]
    return article


@pytest.fixture
def driver():
    return MagicMock()


@pytest.fixture
def scraper(driver):
    instance = SeleniumScraper(driver=driver)
    instance.wait = MagicMock()
    return instance


def test_parse_book_extracts_fields():
    article = make_article("Dune", "£9.99", " In stock ", "star-rating Five")

    book = SeleniumScraper._parse_book(article)

    assert book == {"title": "Dune", "price": "£9.99", "stock": "In stock", "rating": "Five"}


def test_scrape_books_single_page(scraper, driver):
    driver.find_elements.return_value = [make_article("A"), make_article("B")]

    books = scraper.scrape_books(base_url="http://t", max_pages=1)

    assert [book["title"] for book in books] == ["A", "B"]
    driver.get.assert_called_once_with("http://t")
    driver.find_element.assert_not_called()


def test_scrape_books_follows_next_page(scraper, driver):
    driver.find_elements.side_effect = [[make_article("A")], [make_article("B")]]

    books = scraper.scrape_books(max_pages=2)

    assert [book["title"] for book in books] == ["A", "B"]
    driver.find_element.return_value.click.assert_called_once_with()


def test_scrape_books_stops_without_next_link(scraper, driver):
    driver.find_elements.return_value = [make_article("A")]
    driver.find_element.side_effect = NoSuchElementException("no next link")

    books = scraper.scrape_books(max_pages=3)

    assert len(books) == 1


def test_scrape_books_stops_when_next_page_times_out(scraper, driver):
    driver.find_elements.return_value = [make_article("A")]
    scraper.wait.until.side_effect = [None, TimeoutException()]

    books = scraper.scrape_books(max_pages=3)

    assert len(books) == 1


def test_scrape_books_skips_unparseable_items(scraper, driver):
    broken = MagicMock()
    broken.find_element.side_effect = NoSuchElementException("missing")
    driver.find_elements.return_value = [broken, make_article("Valid")]

    books = scraper.scrape_books(max_pages=1)

    assert [book["title"] for book in books] == ["Valid"]


def test_close_quits_driver(scraper, driver):
    scraper.close()

    driver.quit.assert_called_once_with()


def test_constructor_creates_driver_when_not_injected(monkeypatch):
    factory = MagicMock()
    monkeypatch.setattr(selenium_scraper, "create_driver", factory)

    scraper = SeleniumScraper(headless=False)

    assert scraper.driver is factory.return_value
    factory.assert_called_once_with(False)


@pytest.mark.parametrize("headless", [True, False])
def test_create_driver_configures_chrome_options(monkeypatch, headless):
    chrome = MagicMock()
    manager = MagicMock()
    manager.return_value.install.return_value = "/driver"
    monkeypatch.setattr(selenium_scraper.webdriver, "Chrome", chrome)
    monkeypatch.setattr(selenium_scraper, "ChromeDriverManager", manager)
    monkeypatch.setattr(selenium_scraper, "Service", MagicMock())
    monkeypatch.setattr(selenium_scraper, "get_random_user_agent", lambda: "Test-Agent")

    driver = selenium_scraper.create_driver(headless=headless)

    assert driver is chrome.return_value
    arguments = chrome.call_args.kwargs["options"].arguments
    assert ("--headless=new" in arguments) is headless
    assert "user-agent=Test-Agent" in arguments
