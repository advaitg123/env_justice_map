import pandas as pd
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.axes_grid1 import make_axes_locatable

#function to plot map
def plot_on_map (df, var):
	fig, ax = plt.subplots(figsize=(12,12))
	df.plot(ax=ax, column= var, 
	                        cmap='Spectral_r',
	                        legend=True, 
	                       )
	fig.patch.set_visible(False)
	ax.axis('off')
	plt.tight_layout()
	st.write(fig)

#function to plot scatter plot
def plot_scatter(df, vary1, vary2):
	fig = px.scatter(df, x = vary1, y = vary2, trendline="ols", trendline_color_override="red")
	fig.update_layout(height=500, width = 500, showlegend=False)
	st.plotly_chart(fig)

# function to plot histogram
def plot_hist(df, vary):
	fig = px.histogram(df, x=vary)
	fig.update_layout(height=500, width = 500, showlegend=False)
	st.plotly_chart(fig)
