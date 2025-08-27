import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Headphones"],
    "Quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
    "Revenue": [1200, 800, 600, 1100, 700, 300]
}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df,
                       index = "Product",
                       values = "Revenue",
                       columns = "Quarter",
                       fill_value = 0,
                       aggfunc = "sum")
print(pivot)