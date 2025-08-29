import pandas as pd

data = {
    "CustomerID": [301, 302, 303, 304, 305],
    "FullName": ["  Alice Johnson ", "BOB SMITH", "charlie brown", " Diana Prince", "eve ADAMS "],
    "Email": [" alice.j@example.com ", "bob_smith_at_gmail.com", "charlie.b@outlook.com", "diana.p @gmail.com", "eve123@yahoo .com"],
    "City": [" new york ", "CHICAGO", " Miami", "san diego ", "LOS ANGELES "]
}

df = pd.DataFrame(data)
print("Original:\n", df)

df["Cleaned Names"] = df["FullName"].str.strip().str.title()
df["First Name"] = df["Cleaned Names"].str.split(" ").str[0]
df["Last Name"] = df["Cleaned Names"].str.split(" ").str[1]
df["Cleaned Email"] = df["Email"].str.strip()
df["Replaced Email"] = df["Cleaned Email"].str.replace(" ", "").str.replace("_at_", "@")
df["Extracting username before @"] = df["Replaced Email"].str.split("@").str[0]
df["Extracting Domain after @"] = df["Replaced Email"].str.extract(r'@(.+)$')
df["Cleaned City"] = df["City"].str.strip().str.title()
df["Domain Contains gmail"] = df["Replaced Email"].str.contains("gmail")
df["Domain Contains yahoo"] = df["Replaced Email"].str.contains("yahoo")
print(f"Updated Data:", df)
