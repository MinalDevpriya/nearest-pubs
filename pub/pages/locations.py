import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "Resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_cleaned.csv")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.title('Explore Pubs in the UK by Location')
area = st.text_input('Enter a Postal Code or Local Authority')
pubs = df[df['postcode'].str.contains(area, na=False, case=False)]
fig = px.scatter_mapbox(pubs, lat='latitude', lon='longitude', hover_name='name', hover_data=['address', 'local_authority', 'postcode'], zoom=10)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)
