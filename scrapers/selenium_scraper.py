"""
Scraper usando Selenium para sites com JavaScript legado.
"""
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.rate_limiter import get_random_user_agent


class SeleniumScraper:
    """Scraper para sites que dependem de JavaScript."""

    def __init__(self, headless: bool = True):
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"user-agent={get_random_user_agent()}")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_books(self, base_url: str = "https://books.toscrape.com") -> List[Dict]:
        """
        Exemplo: extrai livros do catálogo do site books.toscrape.com.
        """
        books = []
        self.driver.get(base_url)

        # Aguarda carregamento
        self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod"))
        )

        pages_scraped = 0
        while pages_scraped < 3:  # Limite de páginas para demo
            print(f"📄 Processando página {pages_scraped + 1}...")

            articles = self.driver.find_elements(By.CLASS_NAME, "product_pod")
            for article in articles:
                try:
                    books.append({
                        "title": article.find_element(
                            By.CSS_SELECTOR, "h3 a"
                        ).get_attribute("title"),
                        "price": article.find_element(
                            By.CLASS_NAME, "price_color"
                        ).text,
                        "stock": article.find_element(
                            By.CLASS_NAME, "availability"
                        ).text.strip(),
                        "rating": article.find_element(
                            By.CLASS_NAME, "star-rating"
                        ).get_attribute("class").replace("star-rating ", ""),
                    })
                except Exception as e:
                    print(f"⚠️ Erro extraindo livro: {e}")

            # Próxima página
            try:
                next_btn = self.driver.find_element(By.CSS_SELECTOR, "li.next a")
                next_btn.click()
                self.wait.until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod"))
                )
                pages_scraped += 1
            except Exception:
                break

        print(f"✅ Total coletado: {len(books)} livros")
        return books

    def close(self):
        self.driver.quit()
