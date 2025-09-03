import pandas as pd
data = {
    "Employee": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Salary": [35000, 75000, 50000, 120000, 28000],
    "Department": ["HR", "Tech", "Finance", "Tech", "HR"]
}
df = pd.DataFrame(data)
print(df)
df["Tax"] = df["Salary"].apply (lambda x : x * 0.20)
df["Level"] = df["Salary"].apply (lambda x: "Senior" if x >= 70000 else ("Mid" if x <= 69999 and x >= 40000 else "Junior"))
df["Tech Bonus"] = df["Department"].apply (lambda x: 5000 if x == "Tech" else 0)
print("Modified df\n", df)