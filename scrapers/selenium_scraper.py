import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from utils.rate_limiter import get_random_user_agent

logger = logging.getLogger(__name__)

PRODUCT_LOCATOR = (By.CLASS_NAME, "product_pod")


def create_driver(headless: bool = True) -> webdriver.Chrome:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"user-agent={get_random_user_agent()}")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


class SeleniumScraper:
    def __init__(self, headless: bool = True, driver=None):
        self.driver = driver or create_driver(headless)
        self.wait = WebDriverWait(self.driver, 10)

    @staticmethod
    def _parse_book(article) -> dict:
        rating_class = article.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
        return {
            "title": article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title"),
            "price": article.find_element(By.CLASS_NAME, "price_color").text,
            "stock": article.find_element(By.CLASS_NAME, "availability").text.strip(),
            "rating": rating_class.replace("star-rating ", ""),
        }

    def _go_to_next_page(self) -> bool:
        try:
            self.driver.find_element(By.CSS_SELECTOR, "li.next a").click()
            self.wait.until(ec.presence_of_all_elements_located(PRODUCT_LOCATOR))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    def scrape_books(
        self, base_url: str = "https://books.toscrape.com", max_pages: int = 3
    ) -> list[dict]:
        books = []
        self.driver.get(base_url)
        self.wait.until(ec.presence_of_all_elements_located(PRODUCT_LOCATOR))

        for page_number in range(1, max_pages + 1):
            logger.info("Processing page %d", page_number)

            for article in self.driver.find_elements(*PRODUCT_LOCATOR):
                try:
                    books.append(self._parse_book(article))
                except NoSuchElementException as exc:
                    logger.warning("Failed to extract book: %s", exc)

            if page_number == max_pages or not self._go_to_next_page():
                break

        logger.info("Collected %d books", len(books))
        return books

    def close(self) -> None:
        self.driver.quit()
