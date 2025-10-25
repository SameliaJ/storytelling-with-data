# titanic_visuals.py
# Author: Your Name
# Description: Visual analysis of Titanic dataset

import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("Titanic.csv")

# ========================
# 1. Survival by Sex
# ========================

# Group by Sex and calculate totals and survivors
sex_counts = df.groupby('Sex')['Survived'].agg(['count', 'sum'])

plt.figure(figsize=(8, 6))
plt.bar(sex_counts.index, sex_counts['count'], label='Total', color='lightcoral')
plt.bar(sex_counts.index, sex_counts['sum'], label='Survived', color='seagreen')

plt.xlabel("Sex")
plt.ylabel("Number of Passengers")
plt.title("Titanic Survival by Sex")
plt.legend()
plt.show()

# ========================
# 2. Survival by Age Group
# ========================

# Define age bins
age_bins = [0, 18, 30, 40, 50, 60, 100]
age_labels = ['<18', '18-30', '30-40', '40-50', '50-60', '60+']

# Add AgeGroup column
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Group by AgeGroup
age_group_data = df.groupby('AgeGroup')['Survived'].agg(['count', 'sum'])
age_group_data['SurvivalRate'] = (age_group_data['sum'] / age_group_data['count']) * 100

# Plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for total passengers
ax1.bar(age_group_data.index, age_group_data['count'], color='skyblue', label='Total Passengers')
ax1.set_xlabel("Age Group")
ax1.set_ylabel("Total Passengers", color='skyblue')
ax1.set_title("Titanic Survival Rate by Age Group")

# Line plot for survival rate
ax2 = ax1.twinx()
ax2.plot(age_group_data.index, age_group_data['SurvivalRate'], marker='o', color='darkgreen', label='Survival Rate (%)')
ax2.set_ylabel("Survival Rate (%)", color='darkgreen')

# Add grid and show
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='upper right')
plt.show()
