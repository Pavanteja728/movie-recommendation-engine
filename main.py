import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie ratings data
ratings_data = pd.read_csv('ratings.csv')

# Load the movie metadata
movies_metadata = pd.read_csv('movies.csv')

# Merge the ratings and metadata based on movieId
movie_data = pd.merge(ratings_data, movies_metadata, on='movieId')

# Create a pivot table to represent the user ratings matrix
user_ratings_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating').fillna(0)

# Calculate the pairwise cosine similarity between users
user_similarity = cosine_similarity(user_ratings_matrix)

# Function to recommend movies to a user
def recommend_movies(user_id, num_recommendations=5):
    # Get the index of the user
    user_index = user_ratings_matrix.index.get_loc(user_id)
    
    # Calculate the average rating of the user
    user_ratings = user_ratings_matrix.iloc[user_index].values.reshape(1, -1)
    average_rating = user_ratings.mean()
    
    # Calculate the weighted average of user ratings and user similarity
    weighted_ratings = user_similarity[user_index].reshape(1, -1) * (user_ratings - average_rating)
    
    # Calculate the similarity sum
    similarity_sum = user_similarity[user_index].sum().reshape(1, -1)
    
    # Calculate the predicted ratings
    predicted_ratings = average_rating + weighted_ratings / similarity_sum
    
    # Get the indices of the top-rated movies
    top_movies_indices = predicted_ratings.argsort()[0][::-1][:num_recommendations]
    
    # Get the corresponding movie titles
    top_movies = user_ratings_matrix.columns[top_movies_indices]
    
    return top_movies

# Example usage
user_id = 1
recommended_movies = recommend_movies(user_id)
print(f"Recommended movies for User {user_id}:")
for movie in recommended_movies:
    print(movie)
