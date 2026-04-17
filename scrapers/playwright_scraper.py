"""
Scraper assíncrono usando Playwright - moderno e rápido.
"""
import asyncio
from typing import List, Dict
from playwright.async_api import async_playwright


class PlaywrightScraper:
    """Scraper moderno, assíncrono e multi-browser."""

    async def scrape_quotes_async(
        self, base_url: str = "https://quotes.toscrape.com", max_pages: int = 5
    ) -> List[Dict]:
        """
        Scraping assíncrono - várias páginas em paralelo.
        Muito mais rápido que Selenium.
        """
        quotes = []

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()

            # Criar tasks em paralelo
            tasks = []
            for page_num in range(1, max_pages + 1):
                tasks.append(
                    self._scrape_page(context, f"{base_url}/page/{page_num}/")
                )

            results = await asyncio.gather(*tasks, return_exceptions=True)

            for result in results:
                if isinstance(result, list):
                    quotes.extend(result)

            await browser.close()

        print(f"✅ Total coletado: {len(quotes)} quotes (async)")
        return quotes

    async def _scrape_page(self, context, url: str) -> List[Dict]:
        """Extrai quotes de uma única página."""
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=15000)

            quotes = await page.evaluate("""
                () => {
                    const items = document.querySelectorAll('.quote');
                    return Array.from(items).map(q => ({
                        text: q.querySelector('.text')?.innerText || '',
                        author: q.querySelector('.author')?.innerText || '',
                        tags: Array.from(q.querySelectorAll('.tag'))
                            .map(t => t.innerText).join(', ')
                    }));
                }
            """)
            return quotes
        except Exception as e:
            print(f"⚠️ Erro em {url}: {e}")
            return []
        finally:
            await page.close()
