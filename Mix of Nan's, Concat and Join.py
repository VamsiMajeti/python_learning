import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5, 6],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "City": ["New York", "Chicago", np.nan, "San Diego", "Miami", "Chicago"]
})

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105, 106],
    "CustomerID": [1, 2, 2, 7, 3, 5],
    "Amount": [250, np.nan, 300, 400, 150, np.nan]
})

q1_sales = pd.DataFrame({
    "SaleID": [1, 2, 3],
    "CustomerID": [1, 2, 3],
    "Product": ["Laptop", "Phone", "Tablet"],
    "Revenue": [1200, np.nan, 600]
})

q2_sales = pd.DataFrame({
    "SaleID": [4, 5, 6],
    "CustomerID": [2, 4, 5],
    "Product": ["Laptop", "Headphones", "Phone"],
    "Revenue": [1100, 300, np.nan]
})

customers["City"] = customers["City"].fillna("Unknown")

orders_filled = orders.fillna(0)

q1_sales["Revenue"] = q1_sales["Revenue"].fillna(q1_sales["Revenue"].median())
q2_sales["Revenue"] = q2_sales["Revenue"].fillna(q2_sales["Revenue"].median())

merge = pd.merge(customers, orders_filled, on = "CustomerID", how = "inner")
print(merge)

q1_sales["Quarter"] = "Q1"
q2_sales["Quarter"] = "Q2"
all_sales = pd.concat([q1_sales, q2_sales], ignore_index=True)
print(all_sales)

Joining = pd.merge(all_sales, customers, on = "CustomerID", how = "inner")
print(Joining)

Total_revenue_across_Q1_and_Q2 = Joining["Revenue"].sum()
print("Total revenue across Q1 and Q2", Total_revenue_across_Q1_and_Q2)

revenue_per_product = Joining.groupby("Product")["Revenue"].sum()
print("Revenue per product:", revenue_per_product)

orders_per_city = Joining.groupby("City")["Revenue"].count()
print("Orders per city:", orders_per_city)