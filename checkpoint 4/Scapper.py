import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def validate_amazon_url(url):
    pattern = r"(https?://)?(www\.)?amazon\.(com|in|co\.uk|de|ca|fr|co\.jp|it|es|nl|com\.mx|com\.au|com\.br|ae|sg|sa)/.*"
    return bool(re.match(pattern, url))

def fetch_amazon_data(product_link):
    if not validate_amazon_url(product_link):
        raise ValueError("Invalid Amazon product URL.")

    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
    }

    response = requests.get(product_link, headers=request_headers)
    if response.status_code == 200:
        page_content = BeautifulSoup(response.text, 'html.parser')

        # Extract customer reviews
        extracted_reviews = []
        reviews = page_content.select('.review')  # Assuming this is where reviews are extracted
    
        if not reviews:  # If no reviews found
            print("Warning: No reviews found. Amazon might be blocking requests.")
            return None  # Return None instead of an empty DataFrame
    
        for entry in page_content.select('.review'):
            review_body = entry.select_one('.review-text').text.strip() if entry.select_one('.review-text') else None
            if review_body:
                extracted_reviews.append([review_body])

        # Convert to Pandas DataFrame
        df = pd.DataFrame(extracted_reviews, columns=["review_content"])
        return df
    else:
        print("Error: Unable to retrieve data. HTTP Status Code:", response.status_code)
        return pd.DataFrame(columns=["Review Content"])