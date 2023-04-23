import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance
import folium
import os
from matplotlib import image

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "untitled-24 - Twin Perspectives.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_cleaned.csv")



img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)


st.title('Welcome to the Pubs of the UK')
st.image('untitled-24 - Twin Perspectives.jpeg')
st.write('There are a total of', len(df), 'pubs in the dataset')
st.write('Here are some basic statistics about the dataset:')
st.write(df.describe())


