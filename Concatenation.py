import pandas as pd

# Sales data from two months
sales_jan = pd.DataFrame({
    "SaleID": [1, 2, 3],
    "Product": ["Laptop", "Phone", "Tablet"],
    "Amount": [1200, 800, 600]
})

sales_feb = pd.DataFrame({
    "SaleID": [4, 5, 6],
    "Product": ["Laptop", "Phone", "Headphones"],
    "Amount": [1000, 700, 200]
})

print(pd.concat([sales_jan, sales_feb]))

discounts = pd.DataFrame ({1,2,3,4,5})
final = pd.concat([pd.concat([sales_jan, sales_feb]).reset_index(drop = True), discounts], axis = 1)
print(final)