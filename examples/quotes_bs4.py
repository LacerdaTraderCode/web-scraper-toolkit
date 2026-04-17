"""
Exemplo: scraping de quotes usando BeautifulSoup.
Executar: python examples/quotes_bs4.py
"""
import sys
from pathlib import Path

# Adiciona raiz do projeto ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scrapers.bs4_scraper import BeautifulSoupScraper
from utils.exporters import export_all


def main():
    print("🚀 Iniciando scraping com BeautifulSoup...\n")

    scraper = BeautifulSoupScraper(min_interval=1.0)
    try:
        quotes = scraper.scrape_quotes()
        export_all(quotes, "output/quotes_bs4")
    finally:
        scraper.close()

    print("\n✅ Concluído!")


if __name__ == "__main__":
    main()
