#!/usr/bin/env python3

import requests
from io import StringIO
import plotly
import plotly.express as px
import pandas as pd
from State_Conversion import state_conversion

"""
File name: HPAI-map.py
Author: Debra Pacheco
Created: 1/21/25
Version: 1.2
Description:
    This script displays a choropleth map of the United States containing highly pathogenic avian influenza
    cases obtained from the Aphis USDA website.

License: MIT License
"""

url = "https://www.aphis.usda.gov/sites/default/files/hpai-mammals.csv"  # HPAI Detections in mammals from USDA

response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status codes

# Read the content directly into a pandas DataFrame
data = pd.read_csv(StringIO(response.text))

#print(data.tail(30))  # Display the first few rows

# Create a column containing just the year
data['Year'] = pd.DatetimeIndex(data['Date Detected']).year

# Create new column in data with the state abbreviation
data['Abbreviation'] = data['State'].apply(state_conversion)

# Create a new data frame with state counts per year
counts_year = data.groupby(['State', 'Year']).size().reset_index(name='State_Count')

# Create new data frame with total state counts
counts_total = data.groupby(['Abbreviation']).size().reset_index(name='State_Count')

# print(data.head())

# create figure containing total state counts of HPAI in the USA
fig = px.choropleth(counts_total, locations='Abbreviation', locationmode="USA-states", color='State_Count', scope="usa")

fig.show()
