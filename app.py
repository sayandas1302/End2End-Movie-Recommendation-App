import csv
import streamlit as st
import pandas as pd
import requests
import pickle

# loaded artifacts
with open('./artifacts/movie_df.pkl','rb') as file:
    movies_df_new = pd.DataFrame(pickle.load(file))
movie_names = movies_df_new['title']

with open('./artifacts/similarity_score.pkl','rb') as file:
    similarity = pickle.load(file)

cast_and_crew_df = pd.read_csv('./dataset/tmdb_5000_credits.csv')

# UI backend functionality
# =======================================
def recommend(movie_selected):
    index = movies_df_new[movies_df_new['title'] == movie_selected].index[0]
    top_5_recomm = sorted(list(enumerate(similarity[index])), key=lambda x:x[1], reverse=True)[1:6]
    movies_name = [movies_df_new.iloc[movie[0],]['title'] for movie in top_5_recomm]
    movies_id = [movies_df_new.iloc[movie[0],]['id'] for movie in top_5_recomm]
    poster_path = [fetch_poster(movie_id) for movie_id in movies_id]
    return movies_name, poster_path
 
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={apikey}&language=en-US'
    response = requests.get(url).json()
    poster_path = 'https://image.tmdb.org/t/p/w300'+response['poster_path']
    return poster_path
# in the apikey  you have to put the tmdb apikey that you can get after logging in the tmdb website
# this api is required to extract the poster image of the movies 
# for details read the readme.md file

def get_director(obj):
    pass

# buiding the UI
# =======================================

# background
st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("https://miro.medium.com/max/1400/0*EH6n4_TvBJ1OsVsf");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """, unsafe_allow_html=True)

# title
st.markdown(f'''
# Movie Recommendation App
''')

# movie name input
st.markdown(f'''
#### What is your favourite movie?
''')
selected_movie = st.selectbox('',movie_names)
if st.button('Recommend'):
    movies_name, poster_path = recommend(selected_movie)
    
    with st.container():
        st.markdown(f'''
        ### Movies recommended for you
        ''')
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.write(movies_name[0])
            st.image(poster_path[0])

        with col2:
            st.write(movies_name[1])
            st.image(poster_path[1])

        with col3:
            st.write(movies_name[2])
            st.image(poster_path[2])

        with col4:
            st.write(movies_name[3])
            st.image(poster_path[3])

        with col5:
            st.write(movies_name[4])
            st.image(poster_path[4])