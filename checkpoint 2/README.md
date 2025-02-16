# Fake Review Detection - Model Training

This document provides an overview of the model training process, evaluation results, and saved models.

## **Model Training**
- The dataset is split into **80% training** and **20% testing**.
- The following models were trained:
  1. **RandomForestClassifier**
  2. **LogisticRegression**
  3. **MultinomialNB (Naive Bayes)**
  4. **SGDClassifier**
  5. **LightGBM**

## **Evaluation Results (F1 Score)**
| Model               | F1 Score |
|---------------------|---------|
| RandomForest       | 0.8807  |
| LogisticRegression | 0.8976  |
| NaiveBayes        | 0.8696  |
| SGDClassifier      | 0.8987  |
| LightGBM          | 0.8896  |

- **Best Model**: **SGDClassifier** (F1 Score: **0.8987**)

## **Saved Models**
- The best-performing model (`SGDClassifier`) is saved as:
  - `best_model.pkl`
  - The corresponding TF-IDF vectorizer is saved as `tfidf_vectorizer.pkl`.

These models can be loaded for inference to classify new reviews as real or fake.

---

🔥 **Best Model: SGDClassifier (F1: 0.8987)** saved as `best_model.pkl`  
🔥 **TF-IDF Vectorizer** saved as `tfidf_vectorizer.pkl`  
