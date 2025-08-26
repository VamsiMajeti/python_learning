import pandas as pd

Data = {"Customers" : ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "Age" : [25, 32, 40, 29, 37, 45],
        "City" : ["New York", "Chicago", "New York", "San Diego", "Chicago", "New York"],
        "Category" : ["Electronics", "Clothing", "Electronics", "Furniture", "Electronics", "Clothing"],
        "Amount" : [1200, 450, 2200, 800, 1500, 3000]}

df = pd.DataFrame(Data)

result = df.groupby ("City")["Amount"].agg(Total_Revenue = "sum", Average_Spend = "mean", Highest_Purchase = "max", Number_of_Transactions = "count").reset_index()
print(result)
result.to_csv("city_sales.csv", index = False)
result.to_excel("city_sales.xlsx", index = False)
result.to_csv("/Users/vamsi/Documents/Data Analyst Journey/python_learning/city_sales.csv", index=False)