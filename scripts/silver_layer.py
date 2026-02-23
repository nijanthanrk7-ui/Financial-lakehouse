import pandas as pd

df = pd.read_csv("data/bronze_transactions.csv")

# Remove null values
df.dropna(inplace=True)

# Convert date column to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize city names
df["city"] = df["city"].str.title()

df.to_csv("data/silver_transactions.csv", index=False)

print("Silver layer created successfully!")