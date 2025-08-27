import pandas as pd

Data = {"Customers" : ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "Age" : [25, 32, 40, 29, 37, 45],
        "City" : ["New York", "Chicago", "New York", "San Diego", "Chicago", "New York"],
        "Category" : ["Electronics", "Clothing", "Electronics", "Furniture", "Electronics", "Clothing"],
        "Amount" : [1200, 450, 2200, 800, 1500, 3000]}

df = pd.DataFrame(Data)
print(df.groupby(["City", "Category"])["Amount"].agg(
    Total_Revenue="sum",
    Average_Spend="mean",
    Minimum_Purchase="min",
    Number_of_Transactions="count"
))