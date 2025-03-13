from flask import Flask, render_template, request, jsonify
from scraper import scrape_reviews
from model import load_models, classify_reviews
from preprocessing import preprocess_text
import pandas as pd 

app = Flask(__name__)

# Load models
word2vec_model, svm_model = load_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    reviews = scrape_reviews(url)
    if reviews.empty:
        return jsonify({"error": "No reviews found"}), 404
    
    if "Review Text" not in reviews.columns or "Rating" not in reviews.columns:
        return jsonify({"error": "Invalid reviews format"}), 400
    
    preprocessed_reviews = []
    for i, review in enumerate(reviews["Review Text"]):
        review_text = preprocess_text(review)
        rating = reviews.iloc[i]["Rating"]
        preprocessed_reviews.append({"Review Text": review_text, "Rating": rating})
    
    predictions = classify_reviews(preprocessed_reviews, word2vec_model, svm_model)
    
    df = pd.DataFrame({
        "Review": reviews["Review Text"],
        "Rating": reviews["Rating"],
        "Prediction": predictions
    })
    
    # df["Prediction"] = df["Prediction"].map({1: "Fake", 0: "Real"})
    df["Prediction"] = df["Prediction"].map({1: "Fake (Computer Generated)", 0: "Real (Original)"})
    
    result = df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)