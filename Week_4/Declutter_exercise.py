# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:55:38 2024

@author: jbrweelden
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FuncFormatter

# Bar graph exercise

# Data for the bar graph

df = pd.read_excel('Declutter.xlsx')

# Setting up the plot
Months = df['Month']  # Categories for x-axis
Received = df['Ticket Volume Received']
Processed = df['Ticket Volume Processed']

# Create an array with the number of months
x = np.arange(len(Months))

# Bar width
bar_width = 0.35

# Custom colors (hex codes)
Received_color = '#4981c1'
Processed_color = '#da5d5c'

# Plotting the bars
fig, ax = plt.subplots(figsize=(10, 6))

# Bars for 'Received'
bars1 = ax.bar(x - bar_width/2, Received, bar_width, label='Received', color=Received_color)

# Bars for 'Processed'
bars2 = ax.bar(x + bar_width/2, Processed, bar_width, label='Processed', color=Processed_color)

# Adding labels and title
ax.set_xticklabels(Months)
ax.set_title('Ticket Trend')
ax.set_xticks(x)

# Adding data labels on top of the bars
for i in range(len(Months)):
    ax.text(x[i] - bar_width/2, Received[i] + 2, str(Received[i]), ha='center', va='bottom')
    ax.text(x[i] + bar_width/2, Processed[i] + 2, str(Processed[i]), ha='center', va='bottom')

# Setting the y-axis to increment by 50 and format the values with 2 decimal places
ax.yaxis.set_major_locator(MultipleLocator(50))

# Function to format y-axis values to 2 decimal places
ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.2f}'))

# Move the legend to the bottom center
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

ax.grid(True, which='both', axis='y', linestyle='-', linewidth=0.7)
ax.set_axisbelow(True)  # Move gridlines to the background

# Set y-axis limits to 0 and 300
ax.set_ylim(0, 300)

# Show the plot
plt.xticks(rotation=45)
plt.show()

#################################################################################################################

# Step 1: first, we need to convert this into a line graph. 

df = pd.read_excel('Declutter.xlsx')

# Setting up the plot
Months = df['Month']  # Categories for x-axis
Received = df['Ticket Volume Received']
Processed = df['Ticket Volume Processed']

# Plot the line graph
plt.figure(figsize=(10,6))
plt.plot(Months, Received, label="Received")
plt.plot(Months, Processed, label="Processed")

# Add labels and title
plt.ylabel("Tickets received")
plt.title("Ticket trend")
plt.legend()

# Show the plot
plt.show()

#################################################################################################################

# Step 2: Fix the y-axis, should start from 0 and ideally leave some room at the top. 
# clean up x-axis as well. 

df = pd.read_excel('Declutter.xlsx')

# Setting up the plot
Months = df['Month'].apply(lambda x: x[:3])  # Abbreviate month names # Categories for x-axis
Received = df['Ticket Volume Received']
Processed = df['Ticket Volume Processed']

# Plot the line graph
plt.figure(figsize=(10,6))
plt.plot(Months, Received, label="Received")
plt.plot(Months, Processed, label="Processed")

# Add labels and title
plt.ylabel("Tickets received")
plt.title("Ticket trend")
plt.ylim(0, 300)
plt.legend()

# Show the plot
plt.show()

#################################################################################################################

# Step 3: Improve legend and colouring. Make legend directly connected to the lines. Remove spines too.

df = pd.read_excel('Declutter.xlsx')

# Setting up the plot
Months = df['Month'].apply(lambda x: x[:3])  # Abbreviate month names # Categories for x-axis
Received = df['Ticket Volume Received']
Processed = df['Ticket Volume Processed']

# Plot the line graph
plt.figure(figsize=(10,6))
plt.plot(Months, Received, label="Received", color='#47484d')
plt.plot(Months, Processed, label="Processed", color='#0e2180')

# Add labels and title
plt.ylabel("Tickets received")
plt.title("Ticket trend",
          fontsize=16, fontweight='bold', loc='center', pad=15, y=1.05)
plt.ylim(0, 300)
# Annotate the lines with labels directly connected to the lines
for i, label in enumerate(["Received", "Processed"]):
    y = [Received, Processed][i]
    plt.annotate(label, xy=(Months.iloc[-1], y.iloc[-1]), xytext=(5, 0), textcoords='offset points',
                 color=['#47484d', '#0e2180'][i], fontsize=12, ha='left', va='center')

# Delete spines from the box
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Show the plot
plt.show()

#################################################################################################################

# Step 4: Further cleaning of axis, adjust line width and legend font sizes. 

df = pd.read_excel('Declutter.xlsx')

# Setting up the plot
Months = df['Month'].apply(lambda x: x[:3])  # Abbreviate month names # Categories for x-axis
Received = df['Ticket Volume Received']
Processed = df['Ticket Volume Processed']

# Plot the line graph
plt.figure(figsize=(10,6))
plt.plot(Months, Received, label="Received", color='#47484d', linewidth=3)
plt.plot(Months, Processed, label="Processed", color='#0e2180', linewidth=3)

# Add labels and title
plt.ylabel("Tickets received",
           fontsize=12)
plt.title("Ticket trend",
          fontsize=16, fontweight='bold', loc='center', pad=15, y=1.05)
plt.ylim(0, 300)
# Annotate the lines with labels directly connected to the lines
for i, label in enumerate(["Received", "Processed"]):
    y = [Received, Processed][i]
    plt.annotate(label, xy=(Months.iloc[-1], y.iloc[-1]), xytext=(5, 0), textcoords='offset points',
                 color=['#47484d', '#0e2180'][i], fontsize=12, fontweight='bold', ha='left', va='center')

# Delete spines from the box
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Remove tick marks on both x and y axis
ax.tick_params(axis='both', which='both', length=0)

# Make the font size of the data on the axis slightly bigger
ax.tick_params(axis='both', which='major', labelsize=12)

# Show the plot
plt.show()