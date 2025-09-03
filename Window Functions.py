import pandas as pd
data = {
    "Customer": ["Alice", "Alice", "Alice", "Bob", "Bob", "Charlie", "Charlie", "Charlie", "Charlie"],
    "OrderID": [101, 102, 103, 201, 202, 301, 302, 303, 304],
    "OrderDate": [
        "2024-01-05", "2024-01-15", "2024-02-10",
        "2024-01-12", "2024-02-20",
        "2024-01-18", "2024-01-25", "2024-02-02", "2024-03-01"
    ],
    "Amount": [250, 400, 350, 200, 500, 600, 700, 650, 800]
}
df = pd.DataFrame(data)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print("Original Data\n", df)
df["Order Number"] = df.groupby("Customer").cumcount() + 1
df["Rank orders by amount"] = df.groupby("Customer")["Amount"].rank(ascending=False, method="dense")
df["Cumulative sales"] = df.groupby("Customer")["Amount"].cumsum()
df["Running average"] = df.groupby("Customer")["Amount"].expanding().mean().reset_index(level=0, drop=True)
df["Month"] = df["OrderDate"].dt.month
monthly_sales = df.groupby("Month")["Amount"].sum()
print("Added data:\n", df)
print("\nMonthly Total Sales:\n", monthly_sales)