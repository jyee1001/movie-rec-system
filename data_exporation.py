import pandas as pd
import os

# Paths to the datasets
movies_path = '/Users/wxuan/Downloads/ml-latest-small/movies.csv'
ratings_path = '/Users/wxuan/Downloads/ml-latest-small/ratings.csv'
tags_path = '/Users/wxuan/Downloads/ml-latest-small/tags.csv'
links_path = '/Users/wxuan/Downloads/ml-latest-small/links.csv'

# Load each file
movies_df = pd.read_csv(movies_path)
ratings_df = pd.read_csv(ratings_path)
tags_df = pd.read_csv(tags_path)
links_df = pd.read_csv(links_path)

# Merging movies_df with ratings_df (as an example)
combined_df = pd.merge(movies_df, ratings_df, on='movieId')

# Display the first few rows of the merged dataframe
print(combined_df.head())

# save the CSV (path)
output_path = '/Users/wxuan/Downloads/ml-latest-small/combined_data.csv'

# Save the DataFrame to a CSV file
combined_df.to_csv(output_path, index=False)

