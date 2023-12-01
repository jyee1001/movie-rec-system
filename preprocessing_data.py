import pandas as pd
import os

save_path = '/Users/wxuan/Dev/movie-rec-system/combined_df.csv'

# Load the dataset
combined_genre_df = pd.read_csv('/Users/wxuan/Dev/movie-rec-system/combined_df.csv')
combined_genre_df['year'] = combined_genre_df['title'].str.extract(r'\((\d{4})\)').astype(float)
# Assuming 'genres' is the column you want to use, and it's in a format like 'genre1|genre2|genre3'
# Create a new column where genres are concatenated into a single string
combined_genre_df['combined_genres'] = combined_genre_df['genres'].str.replace('|', ' ')
combined_genre_df = combined_genre_df.drop(columns=['genres', 'timestamp'])

# Function to remove the year from the title
def remove_year_from_title(title):
    if " (" in title:
        title = title.rsplit(" (", 1)[0]
    return title

# Assuming 'combined_genre_df' is your DataFrame and it has a column named 'title'
# Apply the function to each title in the DataFrame
combined_genre_df['title'] = combined_genre_df['title'].apply(remove_year_from_title)

# Group by 'movieId' and 'title' and calculate the average rating
avg_rating_df = combined_genre_df.groupby(['movieId', 'title']).rating.mean().reset_index()

# Merge the average rating back with the original DataFrame
merged_df = pd.merge(combined_genre_df.drop(columns=['rating', 'userId']), avg_rating_df, on=['movieId', 'title'])

# Drop duplicate rows to get unique movies
final_df = merged_df.drop_duplicates(subset=['movieId', 'title'])

# Display the first few rows of the final DataFrame
print(final_df.head())


print(combined_genre_df.head())

#combined_genre_df.to_csv(save_path, index=False)


