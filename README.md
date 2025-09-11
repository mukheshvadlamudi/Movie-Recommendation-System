# 🎬 Movie Recommendation System

A simple **movie recommendation web app** built using **Streamlit** and **Python**.  
It recommends movies based on genres using **fuzzy string matching** to find the closest movie title input by the user.

---

## Features

- Search for a movie by name using fuzzy matching.
- Get **5 genre-based recommendations** for similar movies.
- Simple and interactive **Streamlit interface**.
- Works offline using the **MovieLens 100k dataset**.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Movie-Recommendation-System.git
   cd Movie-Recommendation-System

Install dependencies::
  pip install streamlit pandas thefuzz

Make sure you have the dataset:
  Download the https://grouplens.org/datasets/movielens/100k/
  Place the u.item file inside an ml-100k folder in your project.
  
How It Works:
  Fuzzy Matching: Uses thefuzz library to find the closest matching movie title.
  Genre Matching: Recommends movies that share similar genres with the selected movie.
  Random Sampling: Picks 5 movies from the filtered similar movies for variety.

Dependencies:
  Python 3.7+
  Streamlit
  pandas
  thefuzz

Usage:
  streamlit run app.py
Steps:
1.Enter a movie name in the input box.
2.Click Get Recommendations.
3.The app will show the best match and suggest 5 movies with similar genres.

Project Structure:
Movie-Recommendation-System/
│
├─ app.py               # Main Streamlit app
├─ ml-100k/u.item       # MovieLens dataset file
└─ README.md

Future Improvements:
  Integrate larger datasets like MovieLens 25M for modern movies.
  Add movie posters using TMDb API for a more engaging UI.
  Implement rating-based recommendations for better personalization.

Author:
  Mukhesh Vadlamudi
