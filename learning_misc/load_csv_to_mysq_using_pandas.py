# con='genre,artist_name,track_name,track_id,popularity,acousticness,danceability,duration_ms,energy,instrumentalness,key,liveness,loudness,mode,speechiness,tempo,time_signature,valence'
#
# with open('file.txt','w') as file:
#     for word in con.split(','):
#         file.write(f'{word} text,' )
#         file.write('\n')



import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('mysql+pymysql://tableau:password@localhost:3306/spotify')

# Load CSV into a DataFrame
df = pd.read_csv('/Users/ishan.kumar/PycharmProjects/learning_project/learning_kaggle_python/data/spotify_features.csv')

# Insert DataFrame into MySQL table
df.to_sql('spotify', con=engine, if_exists='replace', index=False)

print("Data loaded successfully!")