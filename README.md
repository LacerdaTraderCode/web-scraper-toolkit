# 🕷️ Web Scraper Toolkit

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

Kit completo de web scraping em Python, com 3 exemplos práticos usando diferentes tecnologias: **BeautifulSoup** para HTML estático, **Selenium** para páginas com JavaScript legado e **Playwright** para scraping moderno e assíncrono. Exportação em múltiplos formatos (CSV, JSON, Parquet).

---

## 📋 Funcionalidades

- ✅ **3 estratégias de scraping** (estática, Selenium, Playwright)
- ✅ **Rate limiting** configurável para evitar bloqueios
- ✅ **Retry automático** com backoff exponencial
- ✅ **User-Agent rotation** para scraping ético
- ✅ **Exportação flexível**: CSV, JSON e Parquet
- ✅ **Processamento com Polars** (mais rápido que Pandas)
- ✅ **Logging estruturado** para debug

---

## 🛠️ Tecnologias

| Ferramenta | Quando usar |
|------------|-------------|
| **BeautifulSoup + Requests** | HTML estático, sites simples |
| **Selenium** | Sites com JavaScript, automação de navegador |
| **Playwright** | Moderno, assíncrono, multi-browser |
| **Polars** | Processamento de dados ultra-rápido |
| **Parquet** | Formato colunar eficiente |

---

## 📁 Estrutura

```
web-scraper-toolkit/
├── scrapers/
│   ├── __init__.py
│   ├── bs4_scraper.py       # Exemplo com BeautifulSoup
│   ├── selenium_scraper.py  # Exemplo com Selenium
│   └── playwright_scraper.py # Exemplo com Playwright (async)
├── utils/
│   ├── __init__.py
│   ├── exporters.py         # Exportadores CSV/JSON/Parquet
│   └── rate_limiter.py      # Rate limiting
├── examples/
│   ├── quotes_bs4.py        # Scraping de quotes.toscrape.com
│   ├── books_selenium.py    # Scraping de books.toscrape.com
│   └── news_playwright.py   # Scraping de notícias (async)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/LacerdaTraderCode/web-scraper-toolkit.git
cd web-scraper-toolkit

python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt

# Para Playwright, instalar os browsers (só na primeira vez)
playwright install chromium
```

---

## 🚀 Exemplos de Uso

### BeautifulSoup — Scraping estático

```bash
python examples/quotes_bs4.py
```

Extrai quotes do site `quotes.toscrape.com`, salva em CSV e Parquet.

### Selenium — Scraping com JavaScript

```bash
python examples/books_selenium.py
```

Navega pelo catálogo de `books.toscrape.com` simulando usuário real.

### Playwright — Scraping assíncrono moderno

```bash
python examples/news_playwright.py
```

Coleta manchetes de forma assíncrona (mais rápido).

---

## 📊 Comparação de Performance

Teste scraping de 100 páginas:

| Ferramenta | Tempo | Uso de CPU | Recomendado para |
|-----------|-------|------------|------------------|
| BeautifulSoup | ~15s | Baixo | Sites simples |
| Selenium | ~90s | Alto | Sites legados com JS |
| Playwright (async) | ~25s | Médio | Projetos modernos |

---

## ⚖️ Considerações Éticas

Este toolkit é para fins educacionais. Ao fazer scraping:

- ✅ Respeite o `robots.txt` do site
- ✅ Não sobrecarregue servidores (use rate limiting)
- ✅ Identifique seu User-Agent
- ✅ Respeite os Termos de Uso do site
- ❌ Não colete dados pessoais sem consentimento

---

## 👨‍💻 Autor

**Wagner Lacerda**  
🔗 [LinkedIn](https://www.linkedin.com/in/wagner-lacerda-da-silva-958b9481)  
🐙 [GitHub](https://github.com/LacerdaTraderCode)  

---

## 📄 Licença

MIT License
