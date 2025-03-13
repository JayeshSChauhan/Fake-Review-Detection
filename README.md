# Fake Review Detection System

## Overview
This project is a Fake Review Detection System that identifies whether Amazon product reviews are real or fake. It uses web scraping, text preprocessing, and a machine learning model (SVM) to classify reviews.

## Features
- **Web Scraping:** Extracts reviews from Amazon product pages.
- **Text Preprocessing:** Cleans and processes review text for better model accuracy.
- **Machine Learning Model:** Uses an SVM model to classify reviews.
- **Flask Web App:** Provides a user interface for users to check reviews.

## Project Structure
```
├── app.py                  # Flask API to handle requests
├── model.py                # Loads and applies the SVM model
├── preprocessing.py        # Cleans and processes review text
├── scraper.py              # Scrapes reviews from Amazon
├── SVM_model.pkl           # Trained machine learning model
├── word2vec_model.model    # Word embeddings for text processing
├── static/
│   ├── script.js           # JavaScript for frontend interactions
│   ├── style.css           # Styling for the frontend
├── templates/
│   ├── index.html          # Frontend UI
├── requirements.txt        # Required Python dependencies
├── README.md               # Project documentation
```

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/JayeshSChauhan/Fake-Review-Detection.git
   cd Fake-Review-Detection
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Flask application:**
   ```sh
   python app.py
   ```
2. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```
3. **Enter an Amazon product URL** to analyze reviews.

## Dependencies
```
Flask
BeautifulSoup4
scikit-learn
nltk
requests
word2vec
numpy
pandas
```

**Jayesh S Chauhan**
