import pandas as pd

data = {
    "OrderID": [101, 102, 103, 104],
    "OrderDate": ["2024-01-15", "2024-02-20", "2024-03-05", "2024-03-25"],
    "Amount": [250, 400, 150, 600]
}

df = pd.DataFrame(data)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
print(df)

df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["Day"] = df["OrderDate"].dt.day
df["Weekday"] = df["OrderDate"].dt.day_name()
print(df)

print(df[df["OrderDate"] > "2024-03-01"])

monthly_sales = df.groupby(df["OrderDate"].dt.month)["Amount"].sum()
print(monthly_sales)