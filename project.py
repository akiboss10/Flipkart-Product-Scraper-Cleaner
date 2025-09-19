from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()  # Make sure chromedriver is in PATH
query = "bag"
file = 0

for i in range(1, 10):  # pages 1 to 9
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}")
    time.sleep(2)  # allow page to load

    try:
        elems = driver.find_elements(By.CLASS_NAME, "hCKiGj")
        if not elems:
            print(f"No items found on page {i}")
            continue

        print(f"{len(elems)} item(s) found on page {i}")

        for elem in elems:
            try:
                html_content = elem.get_attribute("outerHTML")
                soup = BeautifulSoup(html_content, "html.parser")
                pretty_html = soup.prettify()

                # Write each product to a separate HTML file
                with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                    f.write(pretty_html)

                file += 1

            except Exception as e:
                print(f"Error processing an element: {e}")

        # Only print summary per page
        print(f"Page {i} completed, total files saved so far: {file}\n")

    except NoSuchElementException:
        print(f"No elements found on page {i}")

driver.quit()
print("Scraping completed! Total files saved:", file)
