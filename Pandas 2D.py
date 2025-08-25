import pandas as pd
data= { "Name" : ["Alice", "Darwin", "Vivian" ],
        "Age" : [25, 27, 29],
        "Department" : ["HR", "Tech", "Sales"]}

df = pd.DataFrame(data)
print(df)
print(df.describe())