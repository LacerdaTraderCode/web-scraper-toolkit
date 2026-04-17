"""
Exemplo: scraping assíncrono com Playwright.
Executar: python examples/news_playwright.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.playwright_scraper import PlaywrightScraper
from utils.exporters import export_all


async def main():
    print("🚀 Iniciando scraping assíncrono com Playwright...\n")

    scraper = PlaywrightScraper()
    quotes = await scraper.scrape_quotes_async(max_pages=5)
    export_all(quotes, "output/quotes_playwright")

    print("\n✅ Concluído!")


if __name__ == "__main__":
    asyncio.run(main())
