# import requests
# from bs4 import BeautifulSoup

# result = requests.get("https://www.tradingview.com/")
# print(result.status_code)

# src = result.content
# print(src)


# Jumia Product Scraper Notebook

import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

# Setup and Constants
JUMIA_URL = 'https://www.jumia.co.ke/flash-sales/?srsltid=AfmBOop8DRMORclQrfhTXQ38AfqYARbzHGLfoRtLVLSsyI1r3jsmtGjE'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def check_website_status(url):
    """Check if the website is accessible"""
    response = requests.get(url, headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Website is accessible.")
        return response.text
    else:
        raise Exception(f"Failed to access the site. Status Code: {response.status_code}")

def extract_product_info(soup):
    """Extract product details from the deals of the week section"""
    products = []
    
    deal_section = soup.find('section', {'data-id': re.compile(r'deals-of-the-week', re.I)})
    if not deal_section:
        print("Could not find the 'Deals of the Week' section.")
        return products

    product_cards = deal_section.find_all('article')
    
    for card in product_cards:
        try:
            name = card.find('h3').text.strip()
            brand = card.get('data-brand') or "Unknown"
            price_tag = card.find('div', class_='prc')
            price = price_tag.text.strip().replace('KSh', '').replace(',', '') if price_tag else '0'

            discount_tag = card.find('div', class_='bdg _dsct')
            discount = discount_tag.text.strip().replace('%', '') if discount_tag else '0'

            rating_tag = card.find('div', class_='stars _s')
            rating = rating_tag['aria-label'].split(' ')[0] if rating_tag else '0'

            reviews_tag = card.find('div', class_='rev')
            reviews = re.findall(r'\d+', reviews_tag.text) if reviews_tag else ['0']
            review_count = reviews[0] if reviews else '0'

            products.append({
                'Product Name': name,
                'Brand Name': brand,
                'Price (Ksh)': float(price),
                'Discount (%)': int(discount),
                'Reviews': int(review_count),
                'Rating': float(rating)
            })
        except Exception as e:
            print(f"Skipping a product due to error: {e}")
    
    return products

def popularity_score(product):
    """Estimate product popularity using custom algorithm"""
    reviews = product['Reviews']
    rating = product['Rating']

    adjusted_rating = ((rating * reviews) + 5 + 1) / (reviews + 2)
    product['Popularity Score'] = round(adjusted_rating * reviews, 2)
    return product

def display_recommendations(products):
    """Display all product recommendations sorted by popularity"""
    print("\n\U0001F4CA Product Recommendations (Sorted by Popularity):\n")
    for idx, p in enumerate(products, 1):
        print(f"{idx}. {p['Product Name']}")
        print(f"   Brand: {p['Brand Name']}")
        print(f"   Price: Ksh {p['Price (Ksh)']}")
        print(f"   Discount: {p['Discount (%)']}%")
        print(f"   Rating: {p['Rating']} ({p['Reviews']} reviews)")
        print(f"   Popularity Score: {p['Popularity Score']}\n")

def to_dataframe(products):
    """Convert to pandas DataFrame"""
    return pd.DataFrame(products)

# Main Execution Block
html = check_website_status(JUMIA_URL)
soup = BeautifulSoup(html, 'html.parser')
products = extract_product_info(soup)

if products:
    popular_products = [popularity_score(p) for p in products]
    popular_products.sort(key=lambda x: x['Popularity Score'], reverse=True)
    display_recommendations(popular_products)

    # Convert to DataFrame
    df = to_dataframe(popular_products)
    df.to_csv("jumia_deals.csv", index=False)
    print("\nCSV export completed: jumia_deals.csv")
else:
    print("No products found.")
