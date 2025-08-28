import pandas as pd

data = {
    "City": ["New York", "Chicago", "New York", "Miami", "Chicago", "Miami"],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Tablet", "Phone"],
    "Revenue": [1200, 800, 600, 1000, 700, 900]
}

df = pd.DataFrame(data)
print(df)

print(df.groupby(["City", "Product"])["Revenue"].agg (["sum", "mean", "count"]))