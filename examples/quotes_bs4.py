import logging

from scrapers.bs4_scraper import BeautifulSoupScraper
from utils.exporters import export_all


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    scraper = BeautifulSoupScraper(min_interval=1.0)
    try:
        quotes = scraper.scrape_quotes()
        export_all(quotes, "output/quotes_bs4")
    finally:
        scraper.close()


if __name__ == "__main__":
    main()
