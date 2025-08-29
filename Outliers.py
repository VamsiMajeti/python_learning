import pandas as pd

data = {
    "CustomerID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"],
    "Purchase": [250, 300, 400, 500, 1000000, 450, 350, 700]  # notice the huge outlier
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

outlier = df[df["Purchase"] > 5000]
print(outlier)

Q1 = df["Purchase"].quantile(0.25)
Q3 = df["Purchase"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outlier_iqr = df[(df["Purchase"] < lower_bound) | (df["Purchase"] > upper_bound)]
print(outlier_iqr)

mean = df["Purchase"].mean()
std = df["Purchase"].std()
df["Zscore"] = (df["Purchase"] - mean) / std
outlier_zscore = df[df["Zscore"].abs() > 3]
print(outlier_zscore)

df_no_outliers = df[(df["Purchase"] >= lower_bound) & (df["Purchase"] <= upper_bound)]
print("\nAfter removing outliers:\n", df_no_outliers)

df_capped = df.copy()
df_capped.loc[df_capped["Purchase"] > upper_bound, "Purchase"] = upper_bound
df_capped.loc[df_capped["Purchase"] < lower_bound, "Purchase"] = lower_bound
print("\nAfter capping outliers:\n", df_capped)

median_value = df["Purchase"].median()
df_replaced = df.copy()
df_replaced.loc[(df_replaced["Purchase"] < lower_bound) | (df_replaced["Purchase"] > upper_bound), "Purchase"] = median_value
print("\nAfter replacing outliers with median:\n", df_replaced)