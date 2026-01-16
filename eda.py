# Exploratory Data Analysis (EDA) using Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [25000, 27000, 30000, 28000, 35000, 40000],
    "Profit": [5000, 6000, 7000, 6500, 9000, 11000]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary:")
print(df.describe())

plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()
