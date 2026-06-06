<div align="center">

# 🕷️ Web Scraper Toolkit

**Kit completo de web scraping com BeautifulSoup, Selenium e Playwright**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-orange)](https://github.com/LacerdaTraderCode/web-scraper-toolkit/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github)](https://github.com/LacerdaTraderCode/web-scraper-toolkit)

</div>

---

## 📌 Sobre o projeto

Kit completo de web scraping em Python com 3 estratégias práticas: **BeautifulSoup** para HTML estático, **Selenium** para páginas com JavaScript legado e **Playwright** para scraping moderno e assíncrono. Inclui rate limiting, retry com backoff exponencial, User-Agent rotation e exportação em CSV, JSON e Parquet.

### Funcionalidades

- ✅ **3 estratégias de scraping** — estática, Selenium, Playwright
- ✅ **Rate limiting** configurável para evitar bloqueios
- ✅ **Retry automático** com backoff exponencial
- ✅ **User-Agent rotation** para scraping ético
- ✅ **Exportação flexível** — CSV, JSON e Parquet
- ✅ **Processamento com Polars** — mais rápido que Pandas
- ✅ **Logging estruturado** para debug

---

## 🛠️ Quando usar cada ferramenta

| Ferramenta | Quando usar |
|------------|-------------|
| **BeautifulSoup + Requests** | HTML estático, sites simples |
| **Selenium** | Sites com JavaScript, automação de navegador |
| **Playwright** | Moderno, assíncrono, suporte multi-browser |
| **Polars** | Processamento de dados ultra-rápido |
| **Parquet** | Armazenamento colunar eficiente |

---

## 📁 Estrutura

```
web-scraper-toolkit/
├── scrapers/
│   ├── bs4_scraper.py        # BeautifulSoup (HTML estático)
│   ├── selenium_scraper.py   # Selenium (JavaScript)
│   └── playwright_scraper.py # Playwright (assíncrono)
├── utils/
│   ├── exporters.py          # Exportadores CSV/JSON/Parquet
│   └── rate_limiter.py       # Rate limiting configurável
├── examples/
│   ├── quotes_bs4.py         # Scraping quotes.toscrape.com
│   ├── books_selenium.py     # Scraping books.toscrape.com
│   └── news_playwright.py    # Scraping de notícias (async)
├── requirements.txt
└── README.md
```

---

## 📦 Instalação

```bash
git clone https://github.com/LacerdaTraderCode/web-scraper-toolkit.git
cd web-scraper-toolkit

python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

# Instalar browsers para Playwright (apenas na primeira vez)
playwright install chromium
```

---

## ⚡ Exemplos de uso

### BeautifulSoup — HTML estático
```bash
python examples/quotes_bs4.py
```
Extrai quotes de `quotes.toscrape.com`, salva em CSV e Parquet.

### Selenium — Sites com JavaScript
```bash
python examples/books_selenium.py
```
Navega pelo catálogo de `books.toscrape.com` simulando usuário real.

### Playwright — Scraping assíncrono
```bash
python examples/news_playwright.py
```
Coleta manchetes de forma assíncrona (mais rápido que Selenium).

---

## 📊 Performance — 100 páginas

| Ferramenta | Tempo | CPU | Recomendado para |
|-----------|-------|-----|------------------|
| BeautifulSoup | ~15s | Baixo | Sites simples |
| Selenium | ~90s | Alto | Sites legados com JS |
| Playwright (async) | ~25s | Médio | Projetos modernos |

---

## ⚖️ Uso ético

Este toolkit é para fins educacionais. Ao fazer scraping:

- ✅ Respeite o `robots.txt` do site
- ✅ Use rate limiting para não sobrecarregar servidores
- ✅ Identifique seu User-Agent corretamente
- ✅ Respeite os Termos de Uso do site
- ❌ Não colete dados pessoais sem consentimento

---

## ✅ Requisitos

- Python **3.11** ou superior

---

## 👤 Autor

<div align="center">

**Wagner Lacerda** — Python Backend Developer | APIs REST • Automação • Data Engineering

[![GitHub](https://img.shields.io/badge/GitHub-LacerdaTraderCode-181717?logo=github&logoColor=white)](https://github.com/LacerdaTraderCode)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Wagner%20Lacerda-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/wagner-lacerda-da-silva-958b9481)
[![YouTube](https://img.shields.io/badge/YouTube-LacerdaTraderCode-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@LacerdaTraderCode)
[![Telegram](https://img.shields.io/badge/Telegram-LacerdaTraderCode-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode)
[![Telegram Bots](https://img.shields.io/badge/Telegram-Bots-26A5E4?logo=telegram&logoColor=white)](https://t.me/LacerdaTraderCode_bots)

📍 Rio Grande do Sul, Brasil

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
