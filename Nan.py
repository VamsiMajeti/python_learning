import pandas as pd
import numpy as np

Data = {
    "Customers": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Age": [25, 32, np.nan, 29, 37, 45],     
    "City": ["New York", "Chicago", "New York", "San Diego", np.nan, "New York"],  
    "Category": ["Electronics", "Clothing", "Electronics", "Furniture", "Electronics", "Clothing"],
    "Amount": [1200, 450, 2200, np.nan, 1500, 3000]  
}

df = pd.DataFrame(Data)
print(df)

print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")
df["Amount"] = df["Amount"].fillna(df["Amount"].median())
print(df)
