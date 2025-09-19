from bs4 import BeautifulSoup
import os
import html
import pandas as pd

# Initialize the dictionary with empty lists
d = {'brand': [], 'description': [], 'price': [], 'product_links': []}

# Get list of files and sort them numerically (bag_0.html, bag_1.html, ...)
files = sorted(os.listdir("data"), key=lambda x: int(x.split('_')[1].split('.')[0]))

for file in files:
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Description
        link_tag = soup.find("a", class_="WKTcLC BwBZTg")
        description = link_tag.get("title") if link_tag else None
        d['description'].append(description)
        print("Description:", description)

        # Product Link
        product_link = "https://www.flipkart.com" + link_tag["href"] if link_tag else None
        d['product_links'].append(product_link)
        print("Product Link:", product_link)

        # Brand
        brand_div = soup.find("div", class_="syl9yP")
        brand = brand_div.get_text(strip=True) if brand_div else None
        d['brand'].append(brand)
        print("Brand:", brand)

        # Price
        price_div = soup.find("div", class_="Nx9bqj")
        price = html.unescape(price_div.get_text(strip=True)) if price_div else None
        d['price'].append(price)
        print("Price:", price)

    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Save to CSV with UTF-8 BOM to preserve ₹ symbol
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")


