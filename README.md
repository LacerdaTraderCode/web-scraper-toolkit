<div align="center">

# 🕷️ Web Scraper Toolkit

**A complete web scraping kit with BeautifulSoup, Selenium, and Playwright**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-orange)](https://github.com/LacerdaTraderCode/web-scraper-toolkit/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/web-scraper-toolkit)

</div>

---

## 📌 About the Project

A complete Python web scraping kit with 3 practical strategies: **BeautifulSoup** for static HTML, **Selenium** for legacy JavaScript-heavy pages, and **Playwright** for modern, asynchronous scraping. Includes rate limiting, retry with exponential backoff, User-Agent rotation, and export to CSV, JSON, and Parquet.

### Features

- ✅ **3 scraping strategies** — static, Selenium, Playwright
- ✅ **Configurable rate limiting** to avoid blocks
- ✅ **Automatic retry** with exponential backoff
- ✅ **User-Agent rotation** for ethical scraping
- ✅ **Flexible export** — CSV, JSON, and Parquet
- ✅ **Polars-based processing** — faster than Pandas
- ✅ **Structured logging** for debugging

---

## 🛠️ When to Use Each Tool

| Tool | When to use |
|------------|-------------|
| **BeautifulSoup + Requests** | Static HTML, simple sites |
| **Selenium** | JavaScript-heavy sites, browser automation |
| **Playwright** | Modern, asynchronous, multi-browser support |
| **Polars** | Ultra-fast data processing |
| **Parquet** | Efficient columnar storage |

---

## 📁 Structure

```
web-scraper-toolkit/
├── scrapers/
│   ├── bs4_scraper.py        # BeautifulSoup (static HTML)
│   ├── selenium_scraper.py   # Selenium (JavaScript)
│   └── playwright_scraper.py # Playwright (asynchronous)
├── utils/
│   ├── exporters.py          # CSV/JSON/Parquet exporters
│   └── rate_limiter.py       # Configurable rate limiting
├── examples/
│   ├── quotes_bs4.py         # Scraping quotes.toscrape.com
│   ├── books_selenium.py     # Scraping books.toscrape.com
│   └── news_playwright.py    # News scraping (async)
├── requirements.txt
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/LacerdaTraderCode/web-scraper-toolkit.git
cd web-scraper-toolkit

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

# Install browsers for Playwright (first time only)
playwright install chromium
```

---

## ⚡ Usage Examples

### BeautifulSoup — static HTML
```bash
python examples/quotes_bs4.py
```
Extracts quotes from `quotes.toscrape.com`, saves to CSV and Parquet.

### Selenium — JavaScript-heavy sites
```bash
python examples/books_selenium.py
```
Navigates the `books.toscrape.com` catalog simulating a real user.

### Playwright — asynchronous scraping
```bash
python examples/news_playwright.py
```
Collects headlines asynchronously (faster than Selenium).

---

## 📊 Performance — 100 pages

| Tool | Time | CPU | Recommended for |
|-----------|-------|-----|------------------|
| BeautifulSoup | ~15s | Low | Simple sites |
| Selenium | ~90s | High | Legacy JS-heavy sites |
| Playwright (async) | ~25s | Medium | Modern projects |

---

## ⚖️ Ethical Use

This toolkit is for educational purposes. When scraping:

- ✅ Respect the site's `robots.txt`
- ✅ Use rate limiting to avoid overloading servers
- ✅ Correctly identify your User-Agent
- ✅ Respect the site's Terms of Use
- ❌ Do not collect personal data without consent

---

## ✅ Requirements

- Python **3.11** or higher

---

## 👤 Author

<div align="center">

**Wagner Lacerda** — Senior Software Engineer | Python, Backend, AI Apps, Automation & Systems

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brazil

</div>

---

## 📄 License

Distributed under the MIT license. See [LICENSE](LICENSE) for more details.
