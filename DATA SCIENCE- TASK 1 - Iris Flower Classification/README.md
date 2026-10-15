# 🌸 Iris Flower Classification
### Oasis Infobyte Internship — Data Science Task 1

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?style=flat-square&logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red?style=flat-square&logo=jupyter)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 📌 Objective

Train and evaluate machine learning classification models to identify the **species of an Iris flower** — *Setosa*, *Versicolor*, or *Virginica* — based on four physical measurements:

| Feature | Description |
|---|---|
| `sepal length (cm)` | Length of the sepal |
| `sepal width (cm)` | Width of the sepal |
| `petal length (cm)` | Length of the petal |
| `petal width (cm)` | Width of the petal |

---

## 🗂️ Project Structure

```
📦 Iris Flower Classification/
├── 📓 iris_classification.ipynb   ← Main Jupyter Notebook (all code & analysis)
└── 📄 README.md                   ← Project documentation (this file)
```

---

## ✅ Feature Checklist

- [x] Load the Iris dataset via `sklearn.datasets.load_iris()` — no external download needed
- [x] Exploratory Data Analysis (EDA): shape, dtypes, null check, descriptive statistics
- [x] Visualisations: pairplot, scatter matrix, and box plots by species
- [x] Feature selection discussion (most discriminative features identified)
- [x] Train / Test split — 80 / 20 using `train_test_split`
- [x] **4 Classifiers trained**: Logistic Regression, K-Nearest Neighbours, Decision Tree, Random Forest
- [x] Evaluation: Accuracy, Confusion Matrix, Classification Report (Precision, Recall, F1)
- [x] Best model identified with justification
- [x] All code in a clean, commented Jupyter Notebook

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation & analysis |
| `numpy` | Numerical operations |
| `matplotlib` | Low-level plotting |
| `seaborn` | Statistical data visualisation |
| `scikit-learn` | Dataset, model training & evaluation |

---

## 🚀 Getting Started

### 1. Clone / Download the repository

```bash
git clone <your-repo-url>
cd "DATA SCIENCE- TASK 1 - Iris Flower Classification"
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook iris_classification.ipynb
```

### 4. Run all cells

Inside Jupyter: **Kernel → Restart & Run All**

---

## 📊 Models Trained & Results Summary

Evaluated on an **80 / 20 stratified split** (30 test samples) and **5-Fold Stratified Cross-Validation**:

| Model | Test Accuracy | 5-Fold CV Mean | CV Std Dev | Primary Advantage |
|---|---|---|---|---|
| **Logistic Regression** | 93.33% | 95.83% | ±2.64% | Fast linear baseline, transparent odds ratios |
| **K-Nearest Neighbours** | 93.33% | **96.67%** | ±3.12% | Highest average cross-validation accuracy |
| **Decision Tree** | 93.33% | 94.17% | ±2.04% | Direct explainability via axis-aligned splits |
| **Random Forest** 🏆 | **93.33%** | **95.00%** | **±1.67%** | **Most stable** (lowest variance) & robust ensemble |

> 🏆 **Best Model: Random Forest Classifier**
> - **Generalization & Stability:** Lowest standard deviation (±1.67%) across folds, proving minimal variance and superior out-of-fold reliability.
> - **Robustness:** Bagging with 100 estimators prevents overfitting on borderline *Versicolor/Virginica* instances.
> - **Feature Interpretability:** Confirms that **Petal Length (44.6%)** and **Petal Width (42.2%)** govern 86.8% of classification importance.

---

## 🔍 Key Findings

1. **Petal Features Dominate:** Petal length and petal width provide the strongest discriminative signal (>86% cumulative importance).
2. **Linear Separability of Setosa:** *Iris-setosa* is 100% linearly separable from *versicolor* and *virginica* across all models (100% precision and recall).
3. **Versicolor vs. Virginica Boundary:** A subtle boundary overlap exists in sepal dimensions between *versicolor* and *virginica*, causing the 2 boundary misclassifications on the test set.
4. **Cross-Validation Reliability:** All models achieve ≥ 94% 5-fold CV accuracy, demonstrating robust generalizability without split bias.

---

## 📚 References

- [scikit-learn Iris Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/supervised_learning.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 👤 Author

**Kanagavel** — Data Science Intern @ Oasis Infobyte
Task 1 · Iris Flower Classification
