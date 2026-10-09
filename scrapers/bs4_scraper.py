import logging

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

from utils.rate_limiter import RateLimiter, get_random_user_agent

logger = logging.getLogger(__name__)


class BeautifulSoupScraper:
    def __init__(self, min_interval: float = 1.0):
        self.rate_limiter = RateLimiter(min_interval)
        self.session = requests.Session()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def fetch(self, url: str) -> BeautifulSoup:
        self.rate_limiter.wait()

        headers = {"User-Agent": get_random_user_agent()}
        response = self.session.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        return BeautifulSoup(response.text, "lxml")

    @staticmethod
    def _parse_quote(div) -> dict:
        tags = [tag.get_text(strip=True) for tag in div.find_all("a", class_="tag")]
        return {
            "text": div.find("span", class_="text").get_text(strip=True),
            "author": div.find("small", class_="author").get_text(strip=True),
            "tags": ", ".join(tags),
        }

    def scrape_quotes(self, base_url: str = "https://quotes.toscrape.com") -> list[dict]:
        quotes = []
        page = 1

        while True:
            logger.info("Scraping page %d", page)
            soup = self.fetch(f"{base_url}/page/{page}/")
            quote_divs = soup.find_all("div", class_="quote")

            if not quote_divs:
                break

            quotes.extend(self._parse_quote(div) for div in quote_divs)

            if not soup.find("li", class_="next"):
                break
            page += 1

        logger.info("Collected %d quotes", len(quotes))
        return quotes

    def close(self) -> None:
        self.session.close()
