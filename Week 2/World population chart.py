# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:47:32 2023

@author: jbrweelden
"""

import plotly.express as px
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("world_population.csv")

# Create the tree map using Plotly Express
fig = px.treemap(df, 
                 path=['Continent', 'Country/Territory'], 
                 values='2022 Population',
                 color='2022 Population',  # You can add color to represent population
                 hover_name='Country/Territory',  # Display country name on hover
                 title='World Population by Country'
                )
fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0)  # Adjust the layout margins for better display
)

# Save the figure as an HTML file
fig.write_html("world_population_treemap.html")