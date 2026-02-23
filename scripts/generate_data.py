import pandas as pd
import random
from faker import Faker

fake = Faker()
data = []

for _ in range(1000):
    data.append({
        "transaction_id": fake.uuid4(),
        "customer_name": fake.name(),
        "amount": round(random.uniform(100, 10000), 2),
        "transaction_date": fake.date_this_year(),
        "city": fake.city()
    })

df = pd.DataFrame(data)
df.to_csv("data/transactions.csv", index=False)

print("Data generated successfully!")