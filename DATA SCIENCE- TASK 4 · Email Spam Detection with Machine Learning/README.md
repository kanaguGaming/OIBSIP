# 📧 Email & SMS Spam Detection using Machine Learning & NLP

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7%2B-orange.svg)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-green.svg)](https://www.nltk.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)]()

> **Oasis Infobyte Internship — Data Science Task 4**  
> **Objective:** Build a Natural Language Processing (NLP) binary classifier that accurately distinguishes spam messages from legitimate (ham) messages.

---

## 📑 Table of Contents
1. [Project Overview](#-project-overview)
2. [Feature Checklist Coverage](#-feature-checklist-coverage)
3. [Dataset Description](#-dataset-description)
4. [NLP Text Preprocessing Pipeline](#-nlp-text-preprocessing-pipeline)
5. [Feature Extraction (TF-IDF Explanation)](#-feature-extraction-tf-idf-explanation)
6. [Machine Learning Models & Results](#-machine-learning-models--results)
7. [In-Depth Discussion: Why Recall is Critical](#-in-depth-discussion-why-recall-is-critical)
8. [Project File Structure](#-project-file-structure)
9. [How to Run](#-how-to-run)
10. [Sample Real-Time Inferences](#-sample-real-time-inferences)

---

## 📌 Project Overview
Unsolicited bulk email ("spam") accounts for a massive proportion of global digital communications, posing severe cybersecurity threats including phishing, ransomware, fraud, and identity theft. This project implements an end-to-end NLP machine learning pipeline that parses, cleans, vectorizes, and classifies text communications with **>98% accuracy and precision**.

---

## ✅ Feature Checklist Coverage
- [x] **Download Suitable Dataset:** Sourced the SMS Spam Collection dataset (`spam.csv`).
- [x] **Data Loading & Class Distribution:** Checked raw counts (4,825 Ham, 747 Spam) and percentage ratios (~87% Ham vs. 13% Spam). Handled duplicate rows (403 duplicates removed).
- [x] **Text Preprocessing Pipeline:** Lowercase normalization, URL and HTML stripping, punctuation/digit removal, NLTK stopword elimination, and Porter stemming.
- [x] **Feature Extraction using TF-IDF:** Converted clean tokens into numerical TF-IDF vectors (3,000 top n-grams) with full mathematical explanations of $TF$, $IDF$, and their combination.
- [x] **Stratified Train/Test Split:** 80% train, 20% test maintaining class ratios.
- [x] **Train Multiple Classifiers:**
  1. **Multinomial Naive Bayes** (Industry gold standard text classifier)
  2. **Support Vector Machine (Linear SVM)**
  3. **Logistic Regression**
- [x] **Comprehensive Evaluation:** Accuracy, Precision, Recall, F1-Score, and visual Confusion Matrix heatmaps.
- [x] **Discussion on Recall:** Detailed markdown analysis detailing why Recall is essential in spam detection and the trade-offs between Type I and Type II errors.
- [x] **(Bonus) WordCloud Visualizations:** High-resolution contrast WordClouds generated for Spam words vs. Ham words.
- [x] **Jupyter Notebook:** All steps documented with rich markdown, interactive charts, and pre-computed outputs in `email_spam_detection.ipynb`.
- [x] **Model Serialization:** Exported `spam_detector_model.pkl` and `tfidf_vectorizer.pkl` for instant production deployment.

---

## 📊 Dataset Description
The dataset is the classic **SMS Spam Collection** originally hosted on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection):
- **Total Raw Records:** 5,572
- **Unique Records After Deduplication:** 5,169
- **Legitimate Messages (`ham`):** 4,516 (87.37%)
- **Spam Messages (`spam`):** 653 (12.63%)
- **Target Encoding:** `ham` $\rightarrow 0$, `spam` $\rightarrow 1$

---

## 🧹 NLP Text Preprocessing Pipeline
Raw human text contains punctuation, slang, emojis, URLs, and frequent stop words that create noise. Our preprocessing function executes:
1. **Case Normalization:** Converts all characters to lowercase.
2. **Regex Cleansing:** Strips web URLs (`http://...`, `www...`), HTML tags, punctuation (`!"#$%...`), and numbers.
3. **Tokenization:** Splits text into constituent words.
4. **Stopword Filtering:** Filters out non-informative English stopwords (via `nltk.corpus.stopwords`).
5. **Porter Stemming:** Reduces words to their morphological base roots (e.g., `calling`, `calls` $\rightarrow$ `call`).

---

## 🧠 Feature Extraction (TF-IDF Explanation)

### What is TF-IDF and What Does It Measure?
Machine learning algorithms operate on numerical vectors. Simple word counts (Bag-of-Words) overestimate words that appear frequently everywhere (like "email", "get", "message").

**TF-IDF** (Term Frequency - Inverse Document Frequency) reflects how important a word is to a specific document within a collection.

1. **Term Frequency (TF):**
   $$\text{TF}(t, d) = \frac{\text{Count of term } t \text{ in document } d}{\text{Total terms in document } d}$$
   Measures how often a word occurs in a specific email.

2. **Inverse Document Frequency (IDF):**
   $$\text{IDF}(t) = \log\left(\frac{1 + N}{1 + \text{DF}(t)}\right) + 1$$
   Measures how rare or informative a word is across all documents $N$. If a word appears in every document, its IDF is minimal; if it only appears in a select few, its IDF is high.

3. **Combined TF-IDF Score:**
   $$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)$$
   High TF-IDF scores are assigned to words that appear often in a single email but rarely across the general corpus (e.g., *"claim"*, *"winner"*, *"urgent"*, *"prize"*).

---

## 🏆 Machine Learning Models & Results

All models were evaluated on an unseen stratified 20% test holdout (1,034 samples):

| Model | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) |
|---|:---:|:---:|:---:|:---:|
| **Support Vector Machine (Linear SVC)** 🥇 | **98.36%** | **98.29%** | **87.79%** | **0.9274** |
| **Multinomial Naive Bayes (Tuned $\alpha=0.2$)** 🥈 | **98.26%** | **96.69%** | **89.31%** | **0.9286** |
| **Logistic Regression ($C=3.0$)** 🥉 | **97.87%** | **99.08%** | **82.44%** | **0.9000** |

### Confusion Matrix Highlights (Best Model - Linear SVM):
- **True Negatives (Ham $\rightarrow$ Ham):** 902 / 903 correctly identified (99.89% precision on legitimate mail)
- **False Positives (Ham $\rightarrow$ Spam):** Only 1 legitimate email flagged
- **True Positives (Spam $\rightarrow$ Spam):** 115 / 131 spam messages blocked
- **False Negatives (Spam $\rightarrow$ Ham):** 16 spam messages slipped through

---

## 🎯 In-Depth Discussion: Why Recall is Critical

### The Precision vs. Recall Trade-Off
In spam detection:
- **Precision:** $\frac{TP}{TP + FP}$ — Out of all messages flagged as spam, how many were actually spam?
- **Recall:** $\frac{TP}{TP + FN}$ — Out of all actual spam messages sent, how many did the filter catch?

### Why Recall is of Utmost Importance:
1. **Cybersecurity & Malicious Payload Containment:**  
   Spam is no longer merely annoying sales promotions. Modern spam contains **credential phishing, banking trojans, ransomware droppers, and social engineering attacks**. A low recall rate means dangerous emails land directly in the user's primary inbox, drastically increasing the likelihood of catastrophic security breaches.
2. **Inbox Overload & User Trust:**  
   If a filter allows 25-35% of spam to leak through (low recall), users are overwhelmed by clutter, defeating the purpose of the spam filtering system.
3. **Quarantine / Spam Folder Safety Net:**  
   In production architectures, detected spam is routed to a **Spam/Junk folder** rather than permanently deleted. High recall ensures threats are quarantined, while giving users a failsafe mechanism to check their spam folder if an unexpected False Positive occurs.

---

## 📁 Project File Structure
```
├── email_spam_detection.ipynb   # Complete interactive Jupyter Notebook with cell outputs & plots
├── spam_detector.py             # Standalone production CLI script for training & inference
├── build_and_run_notebook.py    # Script used to compile and verify notebook cells
├── spam.csv                     # SMS/Email Spam Collection dataset (5,572 rows)
├── spam_detector_model.pkl      # Trained serialized Linear SVM classifier (joblib)
├── tfidf_vectorizer.pkl         # Trained serialized TF-IDF feature extractor (joblib)
├── requirements.txt             # Required Python package dependencies
└── README.md                    # Detailed documentation and project report
```

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Interactive Jupyter Notebook
Open the pre-computed notebook in Jupyter Lab, Jupyter Notebook, or VS Code:
```bash
jupyter notebook email_spam_detection.ipynb
```

### 3. Run Standalone Script / CLI Inference
**Train and evaluate from terminal:**
```bash
python spam_detector.py --train
```

**Test any custom email/SMS string:**
```bash
# Test a spam message:
python spam_detector.py --predict "Claim your free $1000 Walmart gift card now by calling 900-555-1234!"

# Test a legitimate ham message:
python spam_detector.py --predict "Hi team, please find attached the quarterly project review slides for tomorrow's standup."
```

---

## 🔬 Sample Real-Time Inferences

| Input Text | Predicted Class | Spam Probability | Confidence |
|---|:---:|:---:|:---:|
| *"WINNER!! You have been specially selected to receive a £1000 cash prize! Call now to claim."* | `[SPAM]` | **99.12%** | **99.12%** |
| *"Hey Mike, can we reschedule our 3 PM catch-up to tomorrow morning?"* | `[HAM]` | **2.84%** | **97.16%** |
| *"URGENT! Your banking access has been suspended. Click http://bank-verify.net immediately."* | `[SPAM]` | **96.88%** | **96.88%** |
| *"Hi mom, I will be home late tonight, please don't wait for dinner for me."* | `[HAM]` | **1.15%** | **98.85%** |
