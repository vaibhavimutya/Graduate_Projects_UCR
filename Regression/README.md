# Regression, Regularization and Simpson's Paradox

End-to-end implementation of **Linear Regression from scratch** in Python to model 
house sale prices from the Ames Housing dataset. Covers both function approximation 
and probabilistic viewpoints of regression, along with an interesting observation of 
**Simpson's Paradox** in the data.

## Dataset
- **Source:** Ames Housing Dataset (`AmesHousing.txt`)
- **Size:** 2,930 rows, 82 features
- **Features:** 23 nominal, 23 ordinal, 14 discrete, 20 continuous variables
- **Period:** 2006–2010
- **Target:** Sales Price

## What's Covered

### Linear Regression (From Scratch)
- Implemented from both **Function Approximation** and **Probabilistic** viewpoints
- Closed-form solution for regression coefficients (β₀, β₁)
- Handled missing values (NaN) and constant features gracefully

### Regression with Categorical Features
- Modeled SalesPrice as a normal distribution per category
- MLE estimates for category means (μⱼ) and variance (σ²)
- Features ranked from best to worst single-feature estimator by variance

### Regression with Continuous Features
- Simple linear regression per continuous feature
- Features ranked from best to worst single-feature estimator by variance

### Regularization
- Overview of **Ridge (L2)** and **Lasso (L1)** regression as norm constraints on model parameters

### Simpson's Paradox
- Observed a negative correlation between number of kitchens and sale price
- Resolved by conditioning on **Neighbourhood** — houses with 2 kitchens belong to 
  inherently lower-cost neighbourhoods, explaining the paradox

## Key Takeaway
Correlation should never be interpreted causally without conditioning on 
appropriate confounding variables — as demonstrated by the Kitchen/Neighbourhood paradox.

## Run the Notebook
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vaibhavimutya/Graduate_Projects_UCR/blob/main/Regression/House_Price_Prediction.ipynb)
