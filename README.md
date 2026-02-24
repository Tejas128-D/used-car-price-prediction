🚗 Used Car Price Prediction
📌 Project Overview

This project focuses on predicting the market selling price of used cars using Machine Learning.

I built this project to understand the complete ML workflow — from data exploration and feature engineering to model tuning and deployment.

The final model is deployed using Streamlit, where users can select car details and get a predicted price instantly.

🧠 What I Did In This Project
1️⃣ Data Analysis & Cleaning

Explored the dataset to understand price distribution and important features

Selected relevant columns for prediction

Removed unnecessary and leakage-prone features

Applied log transformation to the target variable to improve model stability

2️⃣ Feature Engineering

Selected structured numerical and categorical features

Used ColumnTransformer for preprocessing:

StandardScaler for numerical features

OneHotEncoder for categorical features

3️⃣ Model Comparison

I trained and compared multiple regression models:

Linear Regression

Ridge

Lasso

Support Vector Regression (SVR)

KNN Regressor

Random Forest Regressor

After evaluation, Random Forest performed the best.

4️⃣ Hyperparameter Tuning

Used RandomizedSearchCV to tune Random Forest parameters.

📊 Final Model Performance

R² Score: 0.818

MAE: ₹99,198

RMSE: ₹143,334

The model explains around 82% of the variation in used car prices, which is strong for real-world resale data.

🚀 Deployment

Built an interactive Streamlit web app where users can:

Select brand, fuel type, transmission

Choose registration state and city (dynamic dropdowns)

Enter manufacturing year and mileage

Get predicted selling price with a price range

This helped me understand how ML models are actually deployed in real-world applications.

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Matplotlib

Git & GitHub

📂 Project Structure
used-car-price-prediction/
│
├── app.py
├── final_random_forest_model.pkl
├── cars24_20221210.csv
├── requirements.txt
└── car_price_pridiction_tejas.ipynb
💡 Key Learnings

End-to-end ML pipeline design

Model evaluation using R², MAE, RMSE

Hyperparameter tuning

Avoiding data leakage

Building and deploying ML models

Version control with Git

👨‍💻 About Me

I am currently exploring Data Analytics and Machine Learning, building projects to gain practical experience with real-world datasets and deployment workflows.