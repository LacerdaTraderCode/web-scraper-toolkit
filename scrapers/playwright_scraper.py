import asyncio
import logging

from playwright.async_api import Error, async_playwright

logger = logging.getLogger(__name__)

EXTRACT_QUOTES_SCRIPT = """
() => {
    const items = document.querySelectorAll('.quote');
    return Array.from(items).map(q => ({
        text: q.querySelector('.text')?.innerText || '',
        author: q.querySelector('.author')?.innerText || '',
        tags: Array.from(q.querySelectorAll('.tag')).map(t => t.innerText).join(', ')
    }));
}
"""


class PlaywrightScraper:
    async def scrape_quotes_async(
        self, base_url: str = "https://quotes.toscrape.com", max_pages: int = 5
    ) -> list[dict]:
        quotes = []

        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            try:
                context = await browser.new_context()
                tasks = [
                    self._scrape_page(context, f"{base_url}/page/{page_number}/")
                    for page_number in range(1, max_pages + 1)
                ]
                results = await asyncio.gather(*tasks, return_exceptions=True)
            finally:
                await browser.close()

        for result in results:
            if isinstance(result, list):
                quotes.extend(result)

        logger.info("Collected %d quotes (async)", len(quotes))
        return quotes

    async def _scrape_page(self, context, url: str) -> list[dict]:
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=15000)
            return await page.evaluate(EXTRACT_QUOTES_SCRIPT)
        except Error as exc:
            logger.warning("Failed to scrape %s: %s", url, exc)
            return []
        finally:
            await page.close()
