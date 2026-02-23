import pandas as pd

df = pd.read_csv("data/silver_transactions.csv")

# Total revenue by city
city_revenue = df.groupby("city")["amount"].sum().reset_index()

# Sort highest revenue first
city_revenue = city_revenue.sort_values(by="amount", ascending=False)

city_revenue.to_csv("data/gold_city_revenue.csv", index=False)

print("Gold layer created successfully!")