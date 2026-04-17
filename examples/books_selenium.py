"""
Exemplo: scraping de livros usando Selenium.
Executar: python examples/books_selenium.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.selenium_scraper import SeleniumScraper
from utils.exporters import export_all


def main():
    print("🚀 Iniciando scraping com Selenium...\n")

    scraper = SeleniumScraper(headless=True)
    try:
        books = scraper.scrape_books()
        export_all(books, "output/books_selenium")
    finally:
        scraper.close()

    print("\n✅ Concluído!")


if __name__ == "__main__":
    main()
