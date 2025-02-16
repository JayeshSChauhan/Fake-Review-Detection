# Fake Review Detection Web Application

This web application allows users to detect fake reviews for Amazon products by entering a product URL. The system scrapes the reviews, preprocesses them, and classifies each review as either **real** or **fake** using a trained machine learning model.

## **Website Functionality**
1. **User Input**: The user provides an Amazon product URL through the web interface (`index.html`).
2. **Scraping Reviews**: The backend fetches reviews from Amazon using `Scapper.py`.
3. **Preprocessing**: The extracted reviews are cleaned and transformed using `Preprocessing.py`.
4. **Prediction**: The cleaned data is passed to a **machine learning model** (`best_model.pkl`), which predicts if the reviews are fake or real.
5. **Results Display**: The predictions are displayed on the webpage.

## **Setup Instructions (Run Locally)**
### **1. Clone the Repository**
```sh
git clone https://github.com/your-repository/fake-review-detection.git
cd fake-review-detection
```

### **2. Install Dependencies**
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### **3. Run the Flask App**
```sh
python app.py
```

### **4. Access the Website**
Open your browser and go to:
```
http://127.0.0.1:5000/
```

## **Technologies Used**
- **Frontend**: HTML, CSS, JavaScript (`index.html`)
- **Backend**: Flask (`app.py`)
- **Scraping**: BeautifulSoup (`Scapper.py`)
- **Preprocessing**: NLTK, spaCy (`Preprocessing.py`)
- **Machine Learning**: Logistic Regression (`best_model.pkl`)
- **Data Storage**: Pandas, CSV

## **Project Structure**
```
📂 fake-review-detection
│-- app.py               # Flask backend
│-- Scapper.py           # Amazon review scraper
│-- Preprocessing.py     # Text preprocessing functions
│-- templates/
│   └── index.html       # Web interface
│-- best_model.pkl       # Trained ML model
│-- tfidf_vectorizer.pkl # TF-IDF vectorizer
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation
```

## **Contributing**
Feel free to fork the project and contribute! 🚀

---

🔥 **Start detecting fake reviews now at `http://127.0.0.1:5000/`**  
