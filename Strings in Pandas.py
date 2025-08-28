import pandas as pd
data = {
    "CustomerID": [101, 102, 103, 104, 105],
    "Name": ["  alice  ", "BOB", "  Charlie", "Diana  ", "eVe"],
    "Email": ["alice @example.com", "bob_at_example.com", " charlie@example.com ", "diana@example .com", "eve@example.com "],
    "City": [" new york", "CHICAGO ", "miami", "San Diego ", " LOS ANGELES"]
}
df = pd.DataFrame(data)
print("Original:\n", df)
df["Name"] = df["Name"].str.strip().str.title()
df["Email"] = df["Email"].str.replace(" "," ").str.replace("_at_", "@").str.strip()
df["City"] = df["City"].str.strip().str.title()
df["Valid Email"] = df["Email"].str.contains("@")
print(df)