import pandas as pd

# Read raw transactions
df = pd.read_csv("data/transactions.csv")

# Save as Bronze (raw copy)
df.to_csv("data/bronze_transactions.csv", index=False)

print("Bronze layer created successfully!")