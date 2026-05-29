# DOS Attack Prediction on IPv6 Networks

Detecting Denial-of-Service (DoS) attacks on IPv6 networks using machine learning. 
This project implements PCA-based dimensionality reduction combined with 3 classification 
algorithms on the Kaggle Intrusion Detection dataset.

## Dataset
- **Source:** Kaggle Intrusion Detection Dataset
- **Size:** 25,192 samples, 42 columns (38 numerical, 3 categorical)
- **Classes:** 11,743 anomaly | 13,449 normal

## Methodology
- **One-hot encoding** on categorical features → expanded to 118 features
- **PCA** for dimensionality reduction (99.9% variance retained in just 2 components)
- Custom PCA implementation compared against sklearn PCA (near-identical results)
- Train/test split for model evaluation

## Algorithms Implemented
| Classifier | Accuracy | F1-Score |
|-----------|----------|----------|
| Random Forest | 95.89% | **96.19%** |
| Logistic Regression | 89.7% | 89.7% |
| Naive Bayes | 88.92% | 89.33% |

**Best performing model: Random Forest with 96.19% weighted F1-Score**

## Key Findings
- Random Forest outperforms linear models due to the **non-linear nature of the data**
- Logistic Regression and Naive Bayes are limited by their linear decision boundaries
- Dimensionality reduction via PCA followed by non-linear classification yields strong, generalizable results for network security problems

## Run the Notebook
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vaibhavimutya/Graduate_Projects_UCR/blob/main/DOSAttackPrediction/LogisticRegression.ipynb)
