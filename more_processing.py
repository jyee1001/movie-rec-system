import pandas as pd

# Load the DataFrame
df_path = '/Users/wxuan/Dev/movie-rec-system/combined_df.csv'  # Replace with your file path
combined_df = pd.read_csv(df_path)

# Group by 'movieId' and 'title' and calculate the average rating
avg_rating_df = combined_df.groupby(['movieId', 'title']).rating.mean().reset_index()

# Merge the average rating back with the original DataFrame
merged_df = pd.merge(combined_df.drop(columns=['rating', 'userId']), avg_rating_df, on=['movieId', 'title'])

# Drop duplicate rows to get unique movies
final_df = merged_df.drop_duplicates(subset=['movieId', 'title'])

# Display the first few rows of the final DataFrame
print(final_df.head())

save_path = '/Users/wxuan/Dev/movie-rec-system/combined_df.csv'
final_df.to_csv(save_path, index=False)
