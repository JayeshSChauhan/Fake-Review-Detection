# Amazon Review Scraper

This script scrapes customer reviews from an Amazon product page and saves them into a CSV file.

## **Script Overview**
- The script takes an **Amazon product URL** as input.
- It **validates** the URL format before making a request.
- Uses **BeautifulSoup** to extract review content from the product page.
- Saves the extracted reviews in a CSV file: `Amazon_Reviews.csv`.

## **Requirements**
- Python 3.x
- Required libraries:
  - `requests`
  - `BeautifulSoup` (`bs4`)
  - `csv`
  - `re`

Install dependencies using:
```sh
pip install requests beautifulsoup4
```

## **How It Works**
1. The user provides an **Amazon product URL**.
2. The script sends a **GET request** with headers to avoid bot detection.
3. It extracts **customer reviews** using CSS selectors.
4. The reviews are saved in **Amazon_Reviews.csv**.

## **How to Run**
Run the script using:
```sh
python review_scraper.py
```

When prompted, enter a **valid Amazon product URL**.

## **Output**
- The extracted reviews are saved in `Amazon_Reviews.csv` with a single column:  
  - **Review Content** (The text of each review).

## **Error Handling**
- If an **invalid Amazon URL** is entered, an error message is displayed.
- If the **HTTP request fails**, the script prints the error code.

## **Example**
If a user enters an invalid URL:
```
Enter Amazon product URL: https://invalid-url.com
Output: Invalid Amazon product URL.
```

If the request fails:
```
Error: Unable to retrieve data. HTTP Status Code: 403
```

---

🚀 **Successfully scraped reviews will be saved in `Amazon_Reviews.csv`.**  
