import streamlit as st
import pandas as pd
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
data = pd.read_csv("MOVIE.csv")

# Initialize BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Define functions for encoding text and calculating similarity
def encode_text(text):
    tokens = tokenizer(text, add_special_tokens=True)
    input_ids = torch.tensor(tokens).unsqueeze(0)
    with torch.no_grad():
        outputs = model(input_ids)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def get_recommendations(liked_movie):
    liked_movie_index = data[data["TITLE"] == liked_movie].index[0]
    similarity_matrix = cosine_similarity(encoded_descriptions)
    similar_movie_indices = similarity_matrix[liked_movie_index].argsort()[::-1][1:4]
    recommended_movies = data.loc[similar_movie_indices, "TITLE"].tolist()
    return recommended_movies

# Initialize encoded descriptions
encoded_descriptions = [encode_text(desc) for desc in data["DESCRIPTION"]]

# Streamlit app layout
st.title("Movie Recommender")
user_input = st.text_input("Enter a movie you like:")

if user_input:
    # Check if movie exists in data
    if user_input.upper() not in data["TITLE"].tolist():
        st.error(f"Sorry, we couldn't find '{user_input}'. Please try a different movie.")
    else:
        recommended_movies = get_recommendations(user_input.upper())
        st.success(f"Based on your interest in '{user_input}', we recommend:")
        for movie in recommended_movies:
            st.write(f"- {movie}")
else:
    st.info("Search for a movie or browse through our vast selection!")

