# movie-rec-system
*******Overview*******
This script implements a content-based movie recommendation system using genres as the primary feature.
It utilizes TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction and cosine similarity
for calculating similarities between movies. The system allows users to input a movie title and receive 
recommendations for similar movies based on their content.

*******Script Breakdown*******
Import Libraries
pandas: For data manipulation and analysis.
TfidfVectorizer from sklearn.feature_extraction.text: For converting the genre data into TF-IDF features.
linear_kernel from sklearn.metrics.pairwise: For computing the cosine similarity between movies.
Load and Process Data
data = pd.read_csv('combined_df.csv'): Loads the combined movie dataset.
genre_data = data['combined_genres'].tolist(): Extracts the genre information and converts it into a list.
TF-IDF Vectorization
TfidfVectorizer: Initializes a TF-IDF vectorizer with a maximum of 1000 features and removes English stop words.
tfidf_matrix: Transforms the genre data into a TF-IDF matrix.
Create DataFrame for TF-IDF Features
tfidf_df: A DataFrame representing the TF-IDF features.
Concatenate TF-IDF Features with Original Data
result_df: A DataFrame that combines the original data with the TF-IDF features.
Compute Cosine Similarity Matrix
cosine_sim: A matrix representing the cosine similarity between each pair of movies.
Recommendation Function
recommend_movies_with_scores: A function that takes a movie title and returns the top N similar movies along with their similarity scores.
Main Function
main(): The main function of the script, which runs a user-interactive loop to input movie titles and get recommendations.

*******Usage*******
The user runs the script.
The script prompts the user to enter a movie title.
If the movie is in the dataset, it displays a list of recommended movies based on content similarity.
If the movie is not found, it informs the user and prompts for another title.
The user can exit the script by typing 'exit'.
Example Test Code
The commented-out section under the recommendation function can be used to test the system with a specific movie title.

*******How to Run*******

To use the recommendation system:

Ensure you have the required libraries installed (pandas, sklearn).
Place the combined_df.csv file in the same directory as the script or provide the correct path.
Run the script using a Python interpreter.
Follow the on-screen prompts to input movie titles and receive recommendations.
Notes
The effectiveness of the recommendations depends on the quality and comprehensiveness of the movie genres in the dataset.
The system is currently designed to recommend movies based solely on genre similarity. It can be extended to include other features or more complex algorithms for improved performance.
