from bs4 import BeautifulSoup
import os
import html
import pandas as pd

# Initialize dictionary with empty lists
d = {'brand': [], 'description': [], 'price': [], 'product_links': []}

# Ensure numeric sorting (works for bag_0.html, bag_page_1.html, etc.)
def extract_number(filename):
    nums = ''.join(filter(str.isdigit, filename))
    return int(nums) if nums else -1

files = sorted(os.listdir("data"), key=extract_number)

for file in files:
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Each product card
        products = soup.find_all("div", class_="hCKiGj")
        print(f"📄 {file}: found {len(products)} products")

        for p in products:
            # Description + Link
            link_tag = p.find("a", class_="WKTcLC")
            description = link_tag.get("title") if link_tag else None
            product_link = (
                "https://www.flipkart.com" + link_tag["href"] if link_tag else None
            )

            # Brand
            brand_div = p.find("div", class_="syl9yP")
            brand = brand_div.get_text(strip=True) if brand_div else None

            # Price
            price_div = p.find("div", class_="Nx9bqj")
            price = (
                html.unescape(price_div.get_text(strip=True).replace("₹", "").replace(",", ""))
                if price_div
                else None
            )

            # Append to dict
            d["brand"].append(brand)
            d["description"].append(description)
            d["product_links"].append(product_link)
            d["price"].append(price)

    except Exception as e:
        print(f"⚠ Error processing {file}: {e}")

# Save to CSV
df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")
print(f"\n✅ Extraction complete! {len(df)} products saved to data.csv")
