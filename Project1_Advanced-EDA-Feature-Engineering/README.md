# Project 1: Advanced EDA & Feature Engineering

## Objective
The objective of this project is to transform raw e-commerce transaction data into a clean and machine-learning-ready dataset using data preprocessing, exploratory data analysis (EDA), outlier detection, and feature engineering techniques.

---

## Dataset Information

Dataset Name: Dataset for Data Analytics.csv

Total Records: 1200

Key Columns:
- OrderID
- Date
- Product
- Quantity
- UnitPrice
- PaymentMethod
- OrderStatus
- CouponCode
- ReferralSource
- TotalPrice

---

## Tasks Performed

### 1. Data Cleaning
- Checked dataset structure and missing values.
- Filled missing values in CouponCode using "No Coupon".
- Converted Date column into datetime format.

### 2. Exploratory Data Analysis (EDA)
- Product Distribution Analysis
- Payment Method Analysis
- Total Price Analysis
- Outlier Detection using Boxplot

### 3. Feature Engineering
Created three new features:

#### OrderMonth
Extracted month from order date.

#### AverageItemValue
Calculated using:

AverageItemValue = TotalPrice / Quantity

#### CouponUsed
Binary feature:
- 1 = Coupon Applied
- 0 = No Coupon

### 4. Outlier Detection
Used Interquartile Range (IQR) method to identify outliers in TotalPrice.

Formula:

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## Project Files

- project1.py
- eda_visualization.py
- cleaned_dataset.csv
- Dataset for Data Analytics.csv
- product_distribution.png
- payment_method.png
- outlier_detection.png

---

## Results

Successfully:
- Handled missing values
- Detected outliers using IQR
- Created new predictive features
- Generated visualizations
- Produced a cleaned dataset ready for machine learning

---

## Author

Shivrajsinh Rajput

DecodeLabs Data Science Internship 2026
