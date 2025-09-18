# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:27:11 2023

@author: jbrweelden
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data and adjust formatting

df = pd.read_csv('Week 2.csv')
print(df)

# Combine 'Month' and 'Year' columns into a single 'Date' column
df['Date'] = pd.to_datetime(df['Month'] + ' ' + df['Year'].astype(str))

# Format the 'Date' column to display only year and month
df['Year-Month'] = df['Date'].dt.strftime('%Y-%m')

# Delete the "date" colummn
df = df.drop('Date', axis=1)

#############################################

# Create a Pivot table to summarize amount of deliveries per site

# Summarize data using Pivot by Site
pivot_df = df.pivot_table(index='Site', columns='Supplier', values=['Deliveries'], aggfunc='mean') 

# Print the pivoted DataFrame
print("\nPivoted DataFrame:")
print(pivot_df)

#############################################

# Create a heatmap
sns.heatmap(pivot_df, cmap='coolwarm')

# remove labels
plt.xlabel('')
plt.ylabel('')

# Show the plot
plt.show()

#############################################

# Create line chart based on pivoted DataFrame

pivot_df2 = df.pivot_table(index='Year-Month', 
                           values=['Purchase value'], 
                           aggfunc='mean',
                           )
print(pivot_df2)

# Reset the index to convert the 'Year-Month' column into a regular column
pivot_df2 = pivot_df2.reset_index()

# Create a line chart
plt.plot(pivot_df2['Year-Month'], pivot_df2['Purchase value'], marker='o')

# Set the title for the line chart
plt.title('Purchase Value by Month')

# Set the y-axis label
plt.ylabel('Purchase Value')

# Show the line chart
plt.show()