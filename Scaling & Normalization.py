import pandas as pd

data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Age": [25, 32, 40, 28, 50],
    "Salary": [40000, 52000, 60000, 45000, 120000]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

#Min - Max scaling
df["Salary_MintoMax"] = (df["Salary"] - df["Salary"].min()) / (df["Salary"].max() - df["Salary"].min())
df["Age_MintoMax"] = (df["Age"] - df["Age"].min()) / (df["Age"].max() - df["Age"].min())

#Z - Score
df["Salary_Zscore"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()
df["Age"] = (df["Age"] - df["Age"].mean()) / df["Age"].std()

print("Modified Data:\n", df)