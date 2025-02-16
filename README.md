# Fake Review Detection System

This project is a **Fake Review Detection System** that analyzes Amazon product reviews and classifies them as **real** or **fake** using Machine Learning.

## **Project Overview**
1. **User Input**: The user provides an Amazon product URL.
2. **Scraping**: The system scrapes product reviews from Amazon using `Scapper.py`.
3. **Preprocessing**: The reviews are cleaned and transformed using `Preprocessing.py`.
4. **Model Prediction**: A trained **SGD Regression model** (`best_model.pkl`) predicts whether each review is fake or real.
5. **Web Interface**: Users interact with the system via a Flask-powered website (`index.html`).

## **Project Architecture**
```
📂 
│-- app.py               # Flask backend
│-- Scapper.py           # Amazon review scraper
│-- Preprocessing.py     # Text preprocessing functions
│-- templates/
│   └── index.html       # Web interface
│-- static/              # CSS, JavaScript files (if any)
│-- best_model.pkl       # Trained ML model
│-- tfidf_vectorizer.pkl # TF-IDF vectorizer
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation
```

## **Technologies Used**
- **Programming Language**: Python  
- **Web Framework**: Flask  
- **Frontend**: HTML, CSS, JavaScript  
- **Scraping**: BeautifulSoup  
- **Preprocessing**: NLTK, spaCy  
- **Machine Learning**: Scikit-learn, SGD Regression  
- **Model Deployment**: Flask API  

## **Setup & Installation**
### **1. Clone the Repository**
```sh
git clone https://github.com/your-repository/fake-review-detection.git
cd fake-review-detection
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Run the Flask App**
```sh
python app.py
```

## **How It Works**
1. **User enters an Amazon product URL** on the web interface.
2. **The scraper extracts reviews** from the given product page.
3. **Preprocessing removes noise** (e.g., HTML tags, emojis, stopwords, etc.).
4. **Machine Learning model predicts** whether the reviews are fake or real.
5. **Results are displayed** on the web interface.

## **Outputs**
- **CSV File**: Extracted reviews are saved in `Amazon_Reviews.csv`.
- **Web Interface**: Results are shown with real/fake labels.
  
  ![image](https://github.com/user-attachments/assets/ebbf1b42-d69a-44ee-aefa-079c3a1cf891)
  ![image](https://github.com/user-attachments/assets/2fc2be4f-6f59-4048-a85a-a7d0835c10c3)

## **Contributing**
Feel free to fork this project and contribute! 🚀

## **License**
This project is open-source and free to use.

---

**Jayesh Chauhan**  
