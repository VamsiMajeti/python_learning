import pandas as pd
data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Department": ["HR", "Tech", "Sales", "Tech", "Finance", "HR"],
    "City": ["New York", "Chicago", "Miami", "San Diego", "Chicago", "Miami"]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
df["Label Encode"] = df["Department"].astype("category").cat.codes
Hot_Encode = pd.get_dummies(df, columns=["City"],prefix="City")
print(df)
print(Hot_Encode)