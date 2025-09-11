import streamlit as st
import pandas as pd
from thefuzz import process

# Load dataset
file_path = "ml-100k/u.item"
column_names = ["movie_id", "title", "release_date", "video_release_date", "IMDb_URL", "unknown", 
                "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", 
                "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", 
                "Sci-Fi", "Thriller", "War", "Western"]

movies = pd.read_csv(file_path, sep="|", encoding="latin-1", names=column_names, header=None, usecols=[0, 1, *range(5, 24)])
movies["title"] = movies["title"].str.lower()  # Convert titles to lowercase

# Ensure genre columns are numeric (0 or 1)
genre_columns = movies.columns[2:]  
movies[genre_columns] = movies[genre_columns].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

def find_closest_movie(movie_name):
    """Find the closest matching movie using fuzzy matching."""
    movie_name = movie_name.lower()
    all_titles = movies["title"].tolist()
    best_match, score = process.extractOne(movie_name, all_titles)

    if score > 80:
        movie_details = movies[movies["title"] == best_match].iloc[0]
        return best_match, movie_details["movie_id"]
    return None, None

def get_recommendations(movie_id):
    """Get 5 movie recommendations based on genres."""
    matched_movie = movies[movies["movie_id"] == movie_id].iloc[0]
    genre_mask = matched_movie.iloc[2:].astype(bool)
    similar_movies = movies[movies.iloc[:, 2:].dot(genre_mask) > 0]
    similar_movies = similar_movies[similar_movies["movie_id"] != movie_id]
    return similar_movies.sample(n=5, random_state=42)["title"].tolist()

# Streamlit App
st.title("🎬 Movie Recommendation System")
st.write("Enter a movie name to get recommendations!")

user_input = st.text_input("Enter Movie Name:", "")

if st.button("Get Recommendations"):
    best_match, movie_id = find_closest_movie(user_input)

    if movie_id:
        st.success(f"Best Match: {best_match}")
        recommendations = get_recommendations(movie_id)
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write(f"- {movie}")
    else:
        st.error("Movie not found. Try another title.")
