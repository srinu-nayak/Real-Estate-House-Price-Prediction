# Data Preprocessing on FLATS.CSV
1. loaded the uncleaned flats.csv file
2. It has 3017 rows and 20 columns
3. dataset has null values and no duplicates


# Data Preprocessing on HOUSES.CSV
1. loaded the uncleaned houses.csv file
2. It has 1044 rows and 21 columns
3. dataset has null values and dropped 13 duplicates

Impored the flats_cleaned and house_cleaned datasets
Merged the flats_cleaned and house_cleaned datasets

# Feature engineering on gurgaon_properties_cleaned_v1 file
1. dataset has null values and duplicates
2. fixed all the issues and generated gurgaon_properties_cleaned_v2 file

# Exploratory data analysis 
1. performed univariate analysis
2. performed multivariate analysis
3. performed pandas profiling

# Outlier detection and treatment

# Missing value imputation

# Feature selection and feature engineering
### Technique 1 - Correlation Analysis
### Technique 2 - Random Forest Feature Importance
### Technique 3 - Gradient Boosting Feature importances
### Technique 4 - Permutation Importance
### Technique 5 - LASSO
### Technique 6 - RFE
### Technique 7 - Linear Regression Weights
### Technique 8 - SHAP

# Base model
1. A Pipeline was built using scikit-learn to combine preprocessing and model training steps.
2. The model used was Support Vector Regression (SVR) with a radial basis function (RBF) kernel, which is effective for non-linear relationships.

# Built the best model -  Random Regressor
# Built the UI using python streamlit 

