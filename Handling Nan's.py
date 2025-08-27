import pandas as pd
import numpy as np

Data = {
    "Customer": ["Ivy", "Jack", "Kate", "Leo", "Mona", "Nina", "Oscar", "Paul"],
    "Age": [22, 34, np.nan, 41, 36, np.nan, 50, 28],
    "City": ["Boston", None, "Seattle", "Seattle", "Boston", "Chicago", None, "Chicago"],
    "Category": ["Electronics", "Furniture", "Clothing", None, "Electronics", "Clothing", "Electronics", None],
    "Amount": [500, 2000, np.nan, 1200, 1800, 900, None, 1500]
}

df = pd.DataFrame(Data)
print(df)

print(df.dropna(subset = ["City"]))
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Category"] = df["Category"].fillna("Unknown")
df["Amount"] = df["Amount"].fillna(df["Amount"].median())
print(df)