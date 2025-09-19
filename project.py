from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
query = "bag"
all_links = []

for i in range(1, 10):
    url = f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}"
    driver.get(url)

    try:
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.WKTcLC"))
        )
    except:
        print(f"⚠ No products found on page {i}")
        continue

    for p in products:
        link = p.get_attribute("href")
        if link:
            all_links.append(link)

    print(f"✅ Collected {len(products)} links from page {i}")
    time.sleep(1)

driver.quit()

# Show all links
print(f"\nTotal links collected: {len(all_links)}")
for l in all_links[:10]:  # print first 10 only
    print(l)
