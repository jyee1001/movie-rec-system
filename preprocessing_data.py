import pandas as pd
import os

combined_df = pd.read_csv('/Users/wxuan/Dev/movie-rec-system/combined_data.csv')

#processing the timestamp column into readable format
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], unit='s')

# Splitting the 'genres' into separate genres
genres_dummies = combined_df['genres'].str.get_dummies(sep='|')

# Join these genre columns back to the original dataframe
combined_df = pd.concat([combined_df, genres_dummies], axis=1)

# Extracting year from the title and creating a new column
combined_df['year'] = combined_df['title'].str.extract(r'\((\d{4})\)').astype(float)

print(combined_df.head())

save_path = '/Users/wxuan/Dev/movie-rec-system/combined_df.csv'

combined_df.to_csv(save_path, index=False)
