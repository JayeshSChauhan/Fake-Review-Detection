from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from Scapper import fetch_amazon_data
from Preprocessing import preprocess
import pickle
import pandas as pd

app = Flask(__name__, template_folder="templates")  # Add templates folder
CORS(app)

# Load the trained model and vectorizer
try:
    temp_model = "best_model.pkl"
    temp_vec = "tfidf_vectorizer.pkl"
    with open(temp_model, 'rb') as file:
        model = pickle.load(file)  # Use pickle instead of joblib
    with open(temp_vec, 'rb') as file:
        vectorizer = pickle.load(file)
    print("[INFO] Model and vectorizer loaded successfully")
except Exception as e:
    print(f"[ERROR] Model loading failed: {e}")
    model = None
    vectorizer = None


@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/analyze', methods=['POST'])
def analyze_reviews():
    if model is None or vectorizer is None:
        return jsonify({'error': 'Model or vectorizer not loaded'}), 500
    try:
        data = request.get_json()
        product_url = data.get('product_url')

        if not product_url:
            print("[ERROR] No product URL provided")
            return jsonify({'error': 'Product URL is required'}), 400

        print(f"[INFO] Fetching reviews from {product_url}")
        reviews_df = fetch_amazon_data(product_url)

        if reviews_df is None or reviews_df.empty:
            print("[ERROR] Failed to fetch reviews or empty DataFrame")
            return jsonify({'error': 'Failed to scrape reviews'}), 500

        print("[INFO] Preprocessing reviews...")
        # reviews_df = preprocess(reviews_df)
        reviews_df, _ = preprocess(reviews_df, vectorizer=vectorizer) # Pass the fitted vectorizer

        if reviews_df is None or reviews_df.empty:
            print("[ERROR] Preprocessing failed or empty DataFrame")
            return jsonify({'error': 'Preprocessing failed'}), 500

        # Check DataFrame shape before prediction
        print(f"[INFO] Preprocessed data shape: {reviews_df.shape}")

        # Ensure input format matches model expectation
        if not isinstance(reviews_df, pd.DataFrame):
            print("[ERROR] Preprocessed output is not a DataFrame")
            return jsonify({'error': 'Unexpected preprocessed data format'}), 500

        # Make predictions
        print("[INFO] Making predictions...")
        predictions = model.predict(reviews_df)

        # Prepare the results
        results = []
        for index, prediction in zip(reviews_df.index, predictions): # use reviews_df.index instead of reviews_df
            original_review = fetch_amazon_data(product_url).iloc[index]['review_content']
            results.append({'review': original_review, 'prediction': 'fake' if prediction == 1 else 'real'})

        print("[INFO] Prediction completed successfully")
        return jsonify({'results': results})

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)