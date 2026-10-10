import logging

from scrapers.selenium_scraper import SeleniumScraper
from utils.exporters import export_all


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    scraper = SeleniumScraper(headless=True)
    try:
        books = scraper.scrape_books()
        export_all(books, "output/books_selenium")
    finally:
        scraper.close()


if __name__ == "__main__":
    main()
