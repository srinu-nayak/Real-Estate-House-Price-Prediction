import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='visualization', page_icon="<UNK>")

st.title('Analysis of Real Estate House & Flat Price Prediction')

new_df = pd.read_csv('data/data_viz1.csv')

numeric_cols = ['price','price_per_sqft','built_up_area','latitude','longitude']
group_df = new_df.groupby('sector')[numeric_cols].mean()

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",hover_name=group_df.index, width=1200, height=800)

st.plotly_chart(fig, use_container_width=True)

fig.show()





st.dataframe(new_df)

