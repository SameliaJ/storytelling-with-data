# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:25:54 2024

@author: jbrweelden
"""

import plotly.express as px
import pandas as pd
import numpy as np

# Load the data from the CSV file
df = pd.read_csv("world_population.csv")

# Apply logarithmic transformation to the population values
df['Log Population'] = np.log(df['2022 Population'])

# Create the tree map using Plotly Express
fig = px.treemap(df, 
                 path=['Continent', 'Country/Territory'], 
                 values='2022 Population',  # Use logarithmic scale for population values
                 color='Log Population',  # Use logarithmic scale for color scale
                 color_continuous_scale='BuPu',
                 hover_name='Country/Territory',  # Display country name on hover
                 title='World Population by Country (Log Scale)'
                )

# Manually set the tick values and labels for the color scale
tick_values = np.arange(0, np.ceil(df['Log Population'].max())+1, 1)
tick_labels = np.exp(tick_values).astype(int)

# Format tick labels to display in billions or millions
tick_labels_formatted = []
for label in tick_labels:
    if label >= 1e9:
        tick_labels_formatted.append(f"{label / 1e9:.1f} billion")
    elif label >= 1e6:
        tick_labels_formatted.append(f"{label / 1e6:.1f} million")
    else:
        tick_labels_formatted.append(str(label))

fig.update_coloraxes(colorbar=dict(
    tickvals=tick_values,
    ticktext=tick_labels_formatted
))

fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0)  # Adjust the layout margins for better display
)

# Save the figure as an HTML file
fig.write_html("world_population_treemap_log.html")
