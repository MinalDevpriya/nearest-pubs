import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance
import folium

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_cleaned.csv")

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

def euclidean_distance(x1, y1, x2, y2):
    return distance.euclidean((x1, y1), (x2, y2))

st.title('Find the Nearest Pub')

# get user input for latitude and longitude
lat = st.number_input('Enter your latitude:')
lon = st.number_input('Enter your longitude:')

# calculate distances to all pubs and add as a column to the DataFrame
df['distance_to_user'] = df.apply(lambda row: euclidean_distance(lat, lon, row['latitude'], row['longitude']), axis=1)
nearest_pubs = df.sort_values(by='distance_to_user').head(5)

# create a map centered on the user's location
m = folium.Map(location=[lat, lon], zoom_start=13)

# add markers for the nearest pubs to the map
for index, row in nearest_pubs.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['name'],
        icon=folium.Icon(color='green')
    ).add_to(m)

# display the map
st.write('The nearest pubs to your location are:')
st.write(nearest_pubs[['name', 'address', 'distance_to_user']])
st.write(m)



