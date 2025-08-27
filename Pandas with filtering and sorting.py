import pandas as pd

data = {"Name" : ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Age" : [25, 30, 35, 28, 40],
        "Department" : ["HR", "Tech", "Sales", "Tech", "HR"],
        "Salary" : [50000, 60000, 55000, 65000, 70000]}
df = pd.DataFrame(data)

print(df[["Name", "Department"]])
print(df[(df["Department"] == "Tech") | (df["Salary"] > 65000)])
print(df.sort_values(by="Salary", ascending=False))