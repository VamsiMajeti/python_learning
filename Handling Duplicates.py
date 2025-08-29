import pandas as pd

data = {
    "CustomerID": [201, 202, 203, 204, 201, 205, 206, 202],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Alice", "Eve", "Frank", "Bob"],
    "City": ["New York", "Chicago", "Miami", "San Diego", "New York", "Miami", "Chicago", "Chicago"],
    "Purchase": [250, 300, 400, 500, 250, 600, 700, 300]
}

df = pd.DataFrame(data)
print("Original:\n", df)

print("\nNumber of duplicate rows:", df.duplicated().sum())
df_no_duplicates = df.drop_duplicates()
print("\nAfter removing exact duplicates:\n", df_no_duplicates)
df_unique_names = df.drop_duplicates(subset="Name")
print("\nAfter keeping only first purchase per Name:\n", df_unique_names)