import pandas as pd

data = {
    "OrderID": [301, 302, 303, 304, 305, 306, 307],
    "OrderDate": ["2024-01-10", "2024-01-25", "2024-02-14", "2024-02-28", "2024-03-12", "2024-03-20", "2024-04-05"],
    "Amount": [200, 350, 400, 250, 600, 700, 500]
}

df = pd.DataFrame(data)
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Add date parts
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["Weekday"] = df["OrderDate"].dt.day_name()

# 2. Total sales per quarter
df["Quarter"] = df["OrderDate"].dt.to_period("Q")
quarter_sales = df.groupby("Quarter")["Amount"].sum()

# 3. Average sales per weekday
weekday_avg = df.groupby("Weekday")["Amount"].mean()

# 4. Month with highest sales
monthly_sales = df.groupby("Month")["Amount"].sum().sort_values(ascending=False)

print("Quarterly Sales:\n", quarter_sales, "\n")
print("Average Sales per Weekday:\n", weekday_avg, "\n")
print("Monthly Sales (highest first):\n", monthly_sales, "\n")