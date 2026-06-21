import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("Dataset for Data Analytics.csv")

print("Dataset Shape:", df.shape)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Coupon Codes
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Convert Date Column
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# Feature Engineering
# ---------------------------

# Feature 1
df["OrderMonth"] = df["Date"].dt.month

# Feature 2
df["AverageItemValue"] = (
    df["TotalPrice"] / df["Quantity"]
)

# Feature 3
df["CouponUsed"] = np.where(
    df["CouponCode"] == "No Coupon",
    0,
    1
)

# ---------------------------
# Outlier Detection (IQR)
# ---------------------------

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalPrice"] < lower_bound)
    |
    (df["TotalPrice"] > upper_bound)
]

print("\nOutliers Found:", len(outliers))

# Save Cleaned Dataset
df.to_csv(
    "cleaned_dataset.csv",
    index=False
)

print("\nProject Completed Successfully")
