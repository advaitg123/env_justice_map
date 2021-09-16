import pandas as pd
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#import helper functions for plotting
from plot2 import *

st.set_page_config(page_title = 'Cook County Environmental Justice Data Explorer', 
    layout='wide')

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 415px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 415px;
        margin-left: -415px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)





st.sidebar.title('About')
st.sidebar.write("""

    Are low-income areas in Chicago disproprtionately affected by PM-25 pollution? Which areas in Chicago are at high risk of Cancer 
    due to Air toxins? How do pollution levels vary in different Community Areas in Chicago?
    

    This tool supports analysis of Chicago census block group level data from the  Environmental Protection Agency (EPA). 
    The data is divided into two categories - demographic and environmental. Use the Map feature to see how your variable of 
    interest is distributed around Chicago and your Community Area. Use the Scatter plot to visualise how different variables may be corrlated 
    with each, with a line of best fit. Analyse how a variable is distributed using a histogram to identify interesting peaks and variations. 
    
    More documentation and code details are at the following github repository.https://github.com/advaitg123/env_justice_map/
    """)

st.sidebar.title('Sources')
st.sidebar.write("""
    
    Data was obtained from https://www.epa.gov/ejscreen/download-ejscreen-data    

    Read about the environmental indicators at https://www.epa.gov/ejscreen/overview-environmental-indicators-ejscreen

    Read about the demographic indicators at https://www.epa.gov/ejscreen/overview-demographic-indicators-ejscreen

    """)

st.sidebar.title('Acknowledgment')
st.sidebar.write("""
    
    This app was created by Advait Ganapathy, a Senior at the University of Chicago  

    Advice and mentorship was provided by Raphael Rossellini, a graduate student at the University of Chicago  
    """)

st.title('Chicago Environmental Justice Data Explorer')


comm_areas = pd.read_csv('data/chicago_comm_areas.csv')

df_2020 = pd.read_csv('data/cook_2020_comm_names.csv')

df = gpd.read_file('data/chi_census_blocks.geojson')
df['geoid'] = pd.to_numeric (df['geoid10'])
df['ID'] = df['geoid']//1000

final_df = df.merge(df_2020, left_on='ID', right_on='ID')

st.markdown('## Select the Community Area you wish to further study')

comm_spec = st.selectbox('Community Area : ', list(comm_areas['Name']))

spec_df = final_df[final_df['comm_name'] == comm_spec]
spec_df2 = df_2020[df_2020['comm_name'] == comm_spec]

variables = pd.read_csv('data/variables.csv')
desc = list (variables['Description'])
field = list (variables['GDB Fieldname'])

dic_var = {}

for i in range(len(field)):
    dic_var[desc[i]] = field[i]

st.title('Analyse how the data is distributed on a map')

poll_choice = st.selectbox('Select your Variable choice to plot:', desc)

chicago, community = st.beta_columns(2)
with chicago:
    st.write('Chicago')
    plot_on_map(final_df, dic_var[poll_choice])
with community:
    st.write(comm_spec)
    plot_on_map(spec_df, dic_var[poll_choice])


st.title('Visualise how two variables are associated')

var1 = st.selectbox('Select your first Variable choice to plot on X axis:', desc)
var2 = st.selectbox('Select your second Variable choice to plot on Y Axis:', desc)

chicago, community = st.beta_columns(2)
with chicago:
    st.write('Chicago')
    plot_scatter(df_2020, dic_var [var1], dic_var [var2] )

with community:
    st.write(comm_spec)
    plot_scatter(spec_df2, dic_var [var1], dic_var [var2] )
    

st.title('Dig deeper into the distributed of variable')

va1 = st.selectbox('Select Variable choice to to study data distribution in histogram:', desc)


chicago, community = st.beta_columns(2)
with chicago:
    st.write('Chicago')
    plot_hist(df_2020, dic_var [va1])

with community:
    st.write(comm_spec)
    plot_hist(spec_df2, dic_var [va1])




