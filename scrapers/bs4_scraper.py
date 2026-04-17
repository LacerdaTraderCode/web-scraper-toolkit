"""
Scraper usando BeautifulSoup + Requests para HTML estático.
"""
import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import List, Dict

from utils.rate_limiter import RateLimiter, get_random_user_agent


class BeautifulSoupScraper:
    """Scraper simples e rápido para páginas estáticas."""

    def __init__(self, min_interval: float = 1.0):
        self.rate_limiter = RateLimiter(min_interval)
        self.session = requests.Session()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def fetch(self, url: str) -> BeautifulSoup:
        """Busca uma URL e retorna objeto BeautifulSoup."""
        self.rate_limiter.wait()

        headers = {"User-Agent": get_random_user_agent()}
        response = self.session.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        return BeautifulSoup(response.text, "lxml")

    def scrape_quotes(self, base_url: str = "https://quotes.toscrape.com") -> List[Dict]:
        """
        Exemplo: extrai quotes do site quotes.toscrape.com (site oficial pra aprender).
        """
        quotes = []
        page = 1

        while True:
            url = f"{base_url}/page/{page}/"
            print(f"📄 Scraping página {page}...")

            soup = self.fetch(url)
            quote_divs = soup.find_all("div", class_="quote")

            if not quote_divs:
                break

            for div in quote_divs:
                quotes.append({
                    "text": div.find("span", class_="text").get_text(strip=True),
                    "author": div.find("small", class_="author").get_text(strip=True),
                    "tags": ", ".join(
                        tag.get_text(strip=True)
                        for tag in div.find_all("a", class_="tag")
                    ),
                })

            # Verifica se tem próxima página
            next_btn = soup.find("li", class_="next")
            if not next_btn:
                break
            page += 1

        print(f"✅ Total coletado: {len(quotes)} quotes")
        return quotes

    def close(self):
        self.session.close()
