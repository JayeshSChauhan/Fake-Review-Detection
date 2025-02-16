# Fake Review Detection - Preprocessing

This document provides an overview of the preprocessing steps applied to the dataset for fake review detection.

## **Preprocessing Steps**

1. **Data Loading**
   - The dataset is loaded from `fakeReviewData.csv`.

2. **Language Detection & Translation**
   - `langdetect` is used to identify the language of each review.
   - Non-English reviews are translated into English using `googletrans`.

3. **Text Cleaning**
   - **HTML Tags Removal**: Strips any HTML content.
   - **Links Removal**: Removes URLs from the text.
   - **Punctuation Removal**: Deletes special characters and punctuation.
   - **Stopword Removal**: Eliminates common stopwords using NLTK.
   - **Emoji Conversion**: Converts emojis into text representations.

4. **Tokenization & Lemmatization**
   - Uses **NLTK and spaCy** for tokenization.
   - Lemmatization is applied to reduce words to their root form.

5. **Feature Extraction**
   - **Bag of Words (BoW)**: Converts text into numerical feature vectors using `CountVectorizer`.
   - **TF-IDF**: Applies `TfidfVectorizer` to capture term importance.

6. **Label Encoding**
   - Converts categorical labels into numerical form for model training.

## **Results**
- The dataset is successfully cleaned and transformed.
- The processed text is vectorized using BoW and TF-IDF for further model training.
