import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "Dataset for Data Analytics.csv"
)

# Product Distribution
df["Product"].value_counts().plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Product Distribution")
plt.tight_layout()
plt.savefig("product_distribution.png")
plt.show()

# Payment Method
df["PaymentMethod"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Method Distribution")
plt.savefig("payment_method.png")
plt.show()

# Outlier Detection
plt.boxplot(df["TotalPrice"])

plt.title("Total Price Outliers")
plt.savefig("outlier_detection.png")
plt.show()