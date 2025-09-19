from bs4 import BeautifulSoup
import os
import pandas as pd

# Initialize lists for storing data
brands = []
descriptions = []
prices = []
product_links = []

# Loop through all saved files in "data" folder
for file in sorted(os.listdir("data"), key=lambda x: int(x.split("_")[1].split(".")[0])):
    if file.endswith(".html") and file.startswith("bag_"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "html.parser")

        # Brand
        brand_div = soup.find("div", class_="syl9yP")
        brand = brand_div.get_text(strip=True) if brand_div else None

        # Description
        desc_div = soup.find("a", class_="IRpwTa")
        description = desc_div.get_text(strip=True) if desc_div else None

        # Price
        price_div = soup.find("div", class_="_30jeq3")
        price = price_div.get_text(strip=True) if price_div else None

        # Product link
        link_tag = soup.find("a", href=True)
        link = "https://www.flipkart.com" + link_tag['href'] if link_tag else None

        # Append values to lists
        brands.append(brand)
        descriptions.append(description)
        prices.append(price)
        product_links.append(link)

# Save structured data into CSV
df = pd.DataFrame({
    "Brand": brands,
    "Description": descriptions,
    "Price": prices,
    "Product Link": product_links
})

df.to_csv("data/flipkart_products.csv", index=False, encoding="utf-8")
print("CSV file created with", len(df), "rows")
