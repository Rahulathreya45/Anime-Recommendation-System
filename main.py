import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import  streamlit as st
import os
with open("aligned_data.pkl", "rb") as file:
    aligned_data = pickle.load(file)

# if isinstance(aligned_data, pd.DataFrame):
#     # To display the first few rows of the DataFrame
#     # print(aligned_data.head())
data_dict = aligned_data["name"].to_dict()
# print(data_dict)


# Assuming 'aligned_data' has genre information as feature columns
genre_features = aligned_data[['Unnamed: 0', 'Gourmet', 'Comedy', 'Super Power', 'Fantasy',
       'Shounen-ai', 'Parody', 'Thriller', 'Sports', 'Seinen', 'Military',
       'Music', 'Harem', 'Space', 'Cars', 'Horror', 'Action', 'Shounen',
       'Vampire', 'Detective', 'Samurai', 'Ecchi', 'Drama', 'Dementia', 'Yaoi',
       'Game', 'Shoujo', 'Sci-Fi', 'Work Life', 'Romance', 'Josei', 'Kids',
       'Mecha', 'Martial Arts', 'Historical', 'Police', 'School',
       'Slice of Life', 'Demons', 'Psychological', 'Shoujo-ai', 'Supernatural',
       'Adventure']]  # Replace 'genre1', 'genre2', ... with your actual genre columns
similarity_matrix = cosine_similarity(genre_features, genre_features)

# To find anime similar to a given anime 'target_anime':
target_index = aligned_data.index.get_loc(0)  # Get the index of the target anime
similar_anime_indices = similarity_matrix[target_index].argsort()[-6:][::-1]
similar_anime_indices = similar_anime_indices[similar_anime_indices != target_index]


def get_anime_recommendations(input_anime_name, n=5):
    # Initialize an empty list to store recommendations
    recommendations = []

    # Find the index of the input anime in the data (assuming 'name' is the column with anime names)
    try:
        target_index = aligned_data[aligned_data['name'] == input_anime_name].index[0]

        # Use the similarity matrix to find similar anime
        similar_anime_indices = similarity_matrix[target_index].argsort()[-(n + 1):][::-1]
        similar_anime_indices = similar_anime_indices[similar_anime_indices != target_index]

        # Get the titles of recommended anime
        recommended_anime = [aligned_data.iloc[index]['name'] for index in similar_anime_indices[:n]]

        recommendations.extend(recommended_anime)  # Use extend to add multiple items to the list
    except IndexError:
        recommendations.append("Anime not found in the dataset")

    return recommendations
def count_lines(text):
    return text.count("\n") + 1
base_image_path = 'items/images/images/'
def get_image_path(anime_index):
    return os.path.join(base_image_path, f'{anime_index}.jpg')
# Streamlit app code
st.title("Anime Recommendation System")

anime_name = st.selectbox("Choose an anime", aligned_data["name"])
if st.button("Recommend"):
    recommendations = get_anime_recommendations(anime_name, n=5)

    # Create five separate columns for recommendations
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display each recommendation in its respective column without captions
    for i, anime_name in enumerate(recommendations):
        anime_index = aligned_data[aligned_data['name'] == anime_name].index[0]
        image_path = get_image_path(anime_index)
        num_lines = count_lines(anime_name)
        br_tags = "<br>" * (num_lines - 1)
        if i == 0:
            with col1:
                st.markdown(f"<h3 style='font-size:18px;'>{anime_name}</h3>{br_tags}", unsafe_allow_html=True)
                st.markdown("<style>div { margin-top: 2px; }</style>", unsafe_allow_html=True)# Adjust font size
                st.image(image_path, width=128)
        elif i == 1:
            with col2:
                st.markdown(f"<h3 style='font-size:18px;'>{anime_name}</h3>{br_tags}", unsafe_allow_html=True)
                st.markdown("<style>div { margin-top: 2px; }</style>", unsafe_allow_html=True)
                st.image(image_path, width=128)
        elif i == 2:
            with col3:
                st.markdown(f"<h3 style='font-size:18px;'>{anime_name}</h3>{br_tags}", unsafe_allow_html=True)
                st.markdown("<style>div { margin-top: 2px; }</style>", unsafe_allow_html=True)
                st.image(image_path, width=128)
        elif i == 3:
            with col4:
                st.markdown(f"<h3 style='font-size:18px;'>{anime_name}</h3>{br_tags}", unsafe_allow_html=True)
                st.markdown("<style>div { margin-top: 2px; }</style>", unsafe_allow_html=True)
                st.image(image_path, width=128)
        elif i == 4:
            with col5:
                st.markdown(f"<h3 style='font-size:18px;'>{anime_name}</h3>{br_tags}", unsafe_allow_html=True)
                st.markdown("<style>div { margin-top: 2px; }</style>", unsafe_allow_html=True)
                st.image(image_path, width=128)



