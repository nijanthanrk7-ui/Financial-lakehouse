import pandas as pd
from sqlalchemy import create_engine

# Database connection
username = "postgres"
password = "nijanthan101010"
host = "localhost"
port = "5432"
database = "lakehouse_db"

engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)

# Read Gold data
df = pd.read_csv("data/gold_city_revenue.csv")

# Load into PostgreSQL
df.to_sql("gold_city_revenue", engine, if_exists="replace", index=False)

print("Data loaded to PostgreSQL successfully!")