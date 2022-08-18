import  streamlit as st

import pickle
import pandas as pd
import requests

st.title('Movie Recommender System')


def recommend(movie):
    movie_index = movies[movies['Title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].Title)
        #recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters

movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['Title'].values
)
if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie_name)
    for i in names:
        st.subheader(i)
    