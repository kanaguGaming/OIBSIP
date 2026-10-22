"""
Email / SMS Spam Detection with Machine Learning
Oasis Infobyte - Data Science Task 4

This script provides:
1. Full end-to-end NLP and ML training pipeline
2. Model evaluation comparing Naive Bayes, Linear SVM, and Logistic Regression
3. CLI argument prediction for arbitrary input email/SMS text
"""

import os
import sys
import re
import string
import argparse
import joblib
import pandas as pd
import numpy as np

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Ensure UTF-8 stdout on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Ensure NLTK resources
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()


def clean_text(text: str) -> str:
    """Preprocess raw text: lowercase, strip URLs/HTML/punct, remove stopwords, and apply Porter stemming."""
    text = str(text).lower()
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    text = re.sub(r'<.*?>+', ' ', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub(r'\d+', ' ', text)
    
    words = text.split()
    clean_words = [STEMMER.stem(w) for w in words if w not in STOPWORDS and len(w) > 1]
    return ' '.join(clean_words)


def train_and_evaluate(dataset_path: str = 'spam.csv'):
    """Loads dataset, trains models, evaluates metrics, and saves the best model."""
    print("=" * 75)
    print("  📧 EMAIL / SMS SPAM DETECTION - TRAINING & EVALUATION PIPELINE")
    print("=" * 75)

    if not os.path.exists(dataset_path):
        print(f"Error: Dataset '{dataset_path}' not found!")
        sys.exit(1)

    print(f"\n1. Loading dataset from '{dataset_path}'...")
    df = pd.read_csv(dataset_path, encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'text']
    print(f"   Raw dataset shape: {df.shape}")

    # Remove duplicates
    initial_len = len(df)
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    print(f"   Removed {initial_len - len(df)} duplicate records. Unique samples: {len(df)}")

    # Class distribution
    counts = df['label'].value_counts()
    pcts = df['label'].value_counts(normalize=True) * 100
    print("\n2. Class Distribution:")
    for label in counts.index:
        print(f"   - {label.upper():<4}: {counts[label]:>5} ({pcts[label]:.2f}%)")

    # Target mapping
    df['target'] = df['label'].map({'ham': 0, 'spam': 1})

    print("\n3. Preprocessing text (Tokenization, Stopwords, Stemming)...")
    df['cleaned'] = df['text'].apply(clean_text)

    print("\n4. Performing Stratified 80/20 Train/Test Split...")
    X_train, X_test, y_train, y_test = train_test_split(
        df['cleaned'], df['target'], test_size=0.20, random_state=42, stratify=df['target']
    )
    print(f"   Train samples: {len(X_train)} | Test samples: {len(X_test)}")

    print("\n5. Extracting TF-IDF Features (top 3,000 n-grams)...")
    tfidf = TfidfVectorizer(max_features=3000, ngram_range=(1, 2))
    X_train_vec = tfidf.fit_transform(X_train)
    X_test_vec = tfidf.transform(X_test)
    print(f"   TF-IDF Matrix: {X_train_vec.shape}")

    models = {
        'Multinomial Naive Bayes': MultinomialNB(alpha=0.2),
        'Support Vector Machine (Linear)': SVC(kernel='linear', probability=True, random_state=42),
        'Logistic Regression': LogisticRegression(max_iter=1000, C=3.0, random_state=42)
    }

    print("\n6. Training and Benchmarking Classifiers:")
    print("-" * 75)
    print(f"{'Model Name':<32} {'Accuracy':<10} {'Precision':<11} {'Recall':<10} {'F1-Score':<10}")
    print("-" * 75)

    best_f1 = 0
    best_model = None
    best_name = ""

    for name, model in models.items():
        model.fit(X_train_vec, y_train)
        preds = model.predict(X_test_vec)

        acc = accuracy_score(y_test, preds)
        prec = precision_score(y_test, preds)
        rec = recall_score(y_test, preds)
        f1 = f1_score(y_test, preds)

        print(f"{name:<32} {acc:<10.4f} {prec:<11.4f} {rec:<10.4f} {f1:<10.4f}")

        if f1 > best_f1:
            best_f1 = f1
            best_model = model
            best_name = name

    print("-" * 75)
    print(f"🏆 Best Model based on F1-Score: {best_name} (F1: {best_f1:.4f})")

    # Detailed report for best model
    best_preds = best_model.predict(X_test_vec)
    cm = confusion_matrix(y_test, best_preds)
    print("\n7. Best Model Confusion Matrix:")
    print(f"   TN (Legit -> Legit): {cm[0, 0]:>4} | FP (Legit -> Spam): {cm[0, 1]:>4}")
    print(f"   FN (Spam  -> Legit): {cm[1, 0]:>4} | TP (Spam  -> Spam): {cm[1, 1]:>4}")

    print("\n8. Classification Report:")
    print(classification_report(y_test, best_preds, target_names=['Ham', 'Spam']))

    print("\n9. Serializing artifacts...")
    joblib.dump(best_model, 'spam_detector_model.pkl')
    joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
    print("   ✓ Saved 'spam_detector_model.pkl'")
    print("   ✓ Saved 'tfidf_vectorizer.pkl'")
    print("\nPipeline execution complete!\n")


def predict(text: str):
    """Predicts whether an arbitrary input message is spam or legitimate ham."""
    if not os.path.exists('spam_detector_model.pkl') or not os.path.exists('tfidf_vectorizer.pkl'):
        print("Models not found. Training model first...")
        train_and_evaluate()

    model = joblib.load('spam_detector_model.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')

    cleaned = clean_text(text)
    vec = tfidf.transform([cleaned])

    pred = model.predict(vec)[0]
    probs = model.predict_proba(vec)[0]

    label = "[SPAM] High Risk / Unsolicited" if pred == 1 else "[HAM] Legitimate Message"
    spam_pct = probs[1] * 100
    confidence = probs[pred] * 100

    print("=" * 70)
    print("                 EMAIL SPAM DETECTION INFERENCE")
    print("=" * 70)
    print(f"Raw Input:       \"{text}\"")
    print(f"Preprocessed:    \"{cleaned}\"")
    print(f"Prediction:      {label}")
    print(f"Spam Likelihood: {spam_pct:.2f}%")
    print(f"Confidence:      {confidence:.2f}%")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="NLP Email Spam Detection Classifier")
    parser.add_argument('--train', action='store_true', help="Train models and evaluate metrics")
    parser.add_argument('--predict', type=str, help="Predict if a given string is Spam or Ham")

    args = parser.parse_args()

    if args.predict:
        predict(args.predict)
    elif args.train or len(sys.argv) == 1:
        train_and_evaluate()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
