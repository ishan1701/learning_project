import pandas as pd
from sqlalchemy import create_engine

import pg8000

conn = pg8000.connect(
    host="localhost",
    database="postgres",
    user="tableau",
    password="password"
)
print(conn)
print(conn.__dict__)

df = pd.read_csv('/Users/ishan.kumar/PycharmProjects/learning_project/learning_kaggle_python/data/spotify_features.csv')
engine = create_engine('postgresql+pg8000://tableau:password@localhost:5432/postgres')

# Insert DataFrame into MySQL table
df.to_sql('spotify', schema='spotify', con=engine, if_exists='replace', index=False)

print("Data loaded successfully!")

