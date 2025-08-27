import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "City": ["New York", "Chicago", "Seattle", "Boston", "Miami"]
})
orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "CustomerID": [1, 2, 2, 6, 3],
    "Amount": [250, 450, 300, 700, 150]
})
merge_inner = pd.merge (customers, orders, on = "CustomerID", how = "inner")
merge_right = pd.merge (customers, orders, on = "CustomerID", how = "right")
merge_left = pd.merge (customers, orders, on = "CustomerID", how = "left")
merge_outer = pd.merge (customers, orders, on = "CustomerID", how = "outer")
print(f"Inner join:", merge_inner,"Left merge:", merge_left, "Outer merge:", merge_outer, "Right merge:", merge_right)