from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "bag"
file = 0

for i in range(1, 10):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}")
    elems = driver.find_elements(By.CLASS_NAME, "hCKiGj")
    print(f"{len(elems)} item(s) found on page {i}")

    for elem in elems:
        d = elem.get_attribute("outerHTML")

        # Prettify HTML
        soup = BeautifulSoup(d, "html.parser")
        pretty_html = soup.prettify()

        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(pretty_html)
        file += 1  # move outside "with" to avoid resetting

    time.sleep(2)  # polite wait

driver.close()
