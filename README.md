# Flipkart Product Data Scraper & CSV Generator

**Flipkart Product Data Scraper & CSV Generator** is a Python project that automates the process of collecting, cleaning, and structuring product information from Flipkart. It extracts **brand, product description, price, and product links** from Flipkart product pages, saves raw HTML files locally, and generates a structured CSV file ready for analysis.

---

## Project Workflow

1. **`locating_single.py`**  
   - Scrapes the raw HTML content of Flipkart product pages.  
   - Optionally uses proxies listed in `proxy.txt` for better performance and to avoid IP blocks.  
   - Saves HTML files in the `data/` folder for backup and later processing.

2. **`proxy.txt`**  
   - Contains a list of proxy IP addresses (one per line).  
   - Used by scraping scripts to rotate IPs if required.

3. **`project.py`**  
   - Reads all HTML files from the `data/` folder.  
   - Extracts **brand, description, price, and product links** using BeautifulSoup.  
   - Cleans special characters (like the ₹ symbol) using Python's `html` module.  
   - Saves the structured data to a CSV file (`data.csv`) with UTF-8 encoding for Excel compatibility.

<img width="1586" height="939" alt="Image" src="https://github.com/user-attachments/assets/bff9f4de-5d47-46f0-8ef1-0089231e238c" />

## Features

- Extracts **brand, product description, price, and product links** from Flipkart product pages.  
- Stores raw HTML in `data/` for backup.  
- Cleans and decodes HTML entities like ₹.  
- Generates a structured CSV file ready for analysis.  
- Handles multiple files efficiently and preserves their original order.

---

## Technologies Used

- Python 3.x  
- BeautifulSoup  
- pandas  
- html module  
- Optional: HTTP proxies for scraping

---

## Folder Structure
Flipkart-Product-Scraper/


├── data/ # Raw HTML files from Flipkart

├── proxy.txt # Optional list of proxy IPs

├── locating_single.py # Script to scrape raw HTML pages

├── project.py # Script to parse HTML and generate CSV

├── data.csv # Output CSV file (generated after running project.py)

├── requirements.txt # Python libraries required

└── README.md


---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Flipkart-Product-Scraper.git
   cd Flipkart-Product-Scraper



