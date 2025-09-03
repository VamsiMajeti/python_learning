import pandas as pd
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "City": ["New York", "Chicago", "Seattle", "Miami"]
})
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 2, 3, 4],
    "ProductID": [1001, 1002, 1003, 1001, 1002],
    "Amount": [250, 300, 150, 500, 400]
})
products = pd.DataFrame({
    "ProductID": [1001, 1002, 1003],
    "ProductName": ["Laptop", "Phone", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics"]
})
ctoo = pd.merge(customers, orders, on = "CustomerID", how = "inner")
print("Customers to Orders\n", ctoo)
ctootop = pd.merge(ctoo, products, on = "ProductID", how = "inner")
print("Customers to Orders to Products\n", ctootop)
Total_Sales = ctootop.groupby("City")["Amount"].sum()
print("Total sales\n", Total_Sales)
Average_order = ctootop.groupby("Name")["Amount"].mean()
print("Average order\n", Average_order)
Orders_of_each_product = ctootop.groupby("ProductName")["Category"].count()
print("Orders of each product\n", Orders_of_each_product)