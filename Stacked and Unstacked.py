import pandas as pd

data = {
    "City": ["New York", "Chicago", "New York", "Miami", "Chicago", "Miami", "New York"],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Tablet", "Phone", "Laptop"],
    "Revenue": [1200, 800, 600, 1000, 700, 900, 1100]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# 1. Group by both City and Product, then sum revenue
grouped = df.groupby(["City", "Product"])["Revenue"].sum()
print("\nGrouped (multi-index):\n", grouped)

# 2. Unstack so Products become columns
unstacked = grouped.unstack(fill_value=0)
print("\nUnstacked (Products as columns):\n", unstacked)