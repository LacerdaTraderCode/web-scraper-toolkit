import asyncio
import logging

from scrapers.playwright_scraper import PlaywrightScraper
from utils.exporters import export_all


async def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    scraper = PlaywrightScraper()
    quotes = await scraper.scrape_quotes_async(max_pages=5)
    export_all(quotes, "output/quotes_playwright")


if __name__ == "__main__":
    asyncio.run(main())
