import streamlit as st
import pandas as pd
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data (similar to your code)

# Streamlit app layout
st.title("Movie Recommender")

# User input for liked movie
user_input = st.text_input("Enter a movie you like:")

if user_input:
    # Check if movie exists in data
    if user_input.upper() not in data["TITLE"].str.upper().tolist():
        st.error(f"Sorry, we couldn't find '{user_input}'. Please try a different movie.")
    else:
        # Get recommendations based on user input
        recommended_movies = get_recommendations(user_input.upper())
        st.success(f"Based on your interest in '{user_input}', we recommend:")
        for movie in recommended_movies:
            st.write(f"- {movie}")  # You can display title, description, etc.
else:
    st.info("Search for a movie or browse through our vast selection!")

# Optionally, add search and filter functionalities

