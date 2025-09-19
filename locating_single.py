from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "bag"
for i in range(1, 10):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off")

    elems = driver.find_elements(By.CLASS_NAME, "hCKiGj")
    print(f"{len(elems)} item found")
    for elem in elems:
        print(elem.text)
    time.sleep(5)  # Wait for a while to see the results
driver.close()
