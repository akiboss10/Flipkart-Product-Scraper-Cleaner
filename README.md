# Flipkart Product Data Scraper & CSV Generator

**Flipkart Product Data Scraper & CSV Generator** is a Python project that automates the process of collecting, cleaning, and structuring product information from Flipkart. It extracts **brand, product description, price, and product links** from Flipkart product pages, saves raw HTML files locally, and generates a structured CSV file ready for analysis.

# Web Scraper — `locating_single.py`, `project.py`, `collect.py`

---

## Repository structure

```
├── locating_single.py   # small utility: checks/locates a single page (or local HTML) before scraping
├── project.py           # main scraper that downloads pages and saves raw HTML into `data/`
├── collect.py           # parser: reads HTML files in `data/` and writes structured CSV
├── proxy.txt            # optional: list of proxy IP:PORT (one per line)
├── data/                # folder where raw HTML pages are saved (created by project.py)
├── output.csv           # final CSV produced by collect.py (generated)
└── README.md            # this file
```

---

## Files & responsibilities

### `locating_single.py`

* Purpose: quick check utility to verify whether a given URL (or local HTML file) contains the expected target content (e.g., product container). Use this before running the full scraper to avoid saving irrelevant pages.
* Typical behavior:

  * Accepts a URL or path to a local HTML file.
  * Loads the page (requests / file read), runs a simple BeautifulSoup selector to locate the product block.
  * Returns a short report (found / not found) and optionally prints sample HTML snippet.
* Why use it: speeds development by confirming selectors and avoiding downloading many irrelevant pages.

### `proxy.txt`

* Optional file with a proxy list. Format: one proxy per line, e.g.: `http://12.34.56.78:8080` or `12.34.56.78:8080`.
* `project.py` will read `proxy.txt` if present and rotate proxies between page requests to reduce blocking and improve throughput.
* **Security note:** Keep proxies private. Do not commit sensitive/proprietary proxies to public repositories. Use environment variables or `.gitignore` if needed.

### `project.py` (main scraper)

* Purpose: navigate site(s) and save raw HTML pages in `data/`.
* Features:

  * Takes a list of start URLs (hardcoded or via CLI/config).
  * Uses `requests` or Selenium (commented options) depending on JS requirements.
  * If `proxy.txt` exists, rotates proxies.
  * Saves pages as `data/<basename>_<index>.html` or `data/<query>_<index>.html`.
  * Logs progress: which pages saved, status codes, and any errors to console or a simple log file.
* Error handling: retries on transient failures, polite delays between requests, and respects robots.txt (recommendation).

### `collect.py` (parser & CSV writer)

* Purpose: read saved HTML files from `data/`, parse product details and create `output.csv`.
* Parsing steps:

  1. Iterate over files in `data/`.
  2. Use BeautifulSoup to extract `brand`, `price`, `product_link`, `description` (selectors configurable at top of file).
  3. Normalize/clean strings (strip whitespace, convert rupee/₹ symbols to plain text if needed, convert prices to numeric).
  4. Append results to a list and write a CSV using `pandas` or `csv` module.
* Output columns: `brand`, `description`, `price`, `product_link`, `source_file`.
* Recommended: include basic duplicate detection (by `product_link` or normalized title) before writing CSV.

---

## Quick start

1. Create a Python virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```


2. (Optional) Fill `proxy.txt` with proxies (one per line) if you want proxy rotation.

3. Run a single-location check with `locating_single.py` to verify selectors:

```bash
python locating_single.py --url "https://example.com/product-page.html"
```

4. Run the main scraper to populate `data/`:

```bash
python project.py --start-urls urls.txt --max-pages 200
```

5. Parse saved HTML files and create CSV:

```bash
python collect.py --data-dir data --output output.csv
```

---

## Configuration & tips

* **Selectors:** Keep CSS selectors at the top of `collect.py` or in a separate `config.json` so you can tweak them without changing core code.
* **Respect site rules:** Honor `robots.txt` and throttle requests (`time.sleep`) to avoid overloading servers or getting blocked.
* **Proxy usage:** Test each proxy for connectivity before using it; many free proxies are unreliable.
* **User agent:** Set a realistic `User-Agent` header; rotate if necessary.
* **Logging:** Add a rotating log file or simple CSV log for failed pages to rerun later.
* **Avoid committing `data/` or `proxy.txt` to public repo:** add them to `.gitignore`.

---

## Troubleshooting

* If `collect.py` misses many items, verify the HTML saved in `data/` contains the product elements and that selectors in `collect.py` match the structure.
* If pages are blank or dynamic content is missing, switch `project.py` to use Selenium or another browser automation tool to render JavaScript.

---

## License

MIT

---

## Next steps / improvements

* Parallel downloads with careful rate-limiting.
* Add robust deduplication and canonicalization of product links.
* Implement a small SQLite DB to store scraped items and incremental runs.
* Add unit tests for parsing functions.

