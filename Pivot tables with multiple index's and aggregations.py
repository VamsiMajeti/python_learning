import pandas as pd

data = {
    "CustomerID": [1, 2, 3, 2, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Bob", "Diana", "Eve"],
    "City": ["New York", "Chicago", "Seattle", "Chicago", "San Diego", "Miami"],
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Headphones", "Phone"],
    "Quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
    "Revenue": [1200, 800, 600, 1100, 300, 700]
}

df = pd.DataFrame(data)

pivot = pd.pivot_table(df,
                 index= ["City", "Quarter"],
                 columns= "Product",
                 values= "Revenue",
                 aggfunc = ["sum", "mean", "count"],
                 fill_value = 0,
                 margins = True,
                 margins_name = "Total")
print(pivot)