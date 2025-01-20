import requests
from io import StringIO
import plotly
import plotly.express as px
import pandas as pd



url = "https://www.aphis.usda.gov/sites/default/files/hpai-mammals.csv"  # HPAI Detections in mammals from USDA

response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status codes

# Read the content directly into a pandas DataFrame
data = pd.read_csv(StringIO(response.text))

# print(data.head())  # Display the first few rows

# Create a column containing just the year
data['Year'] = pd.DatetimeIndex(data['Date Detected']).year

# Create a new data frame with state counts per year
counts_year = data.groupby(['State', 'Year']).size().reset_index(name='State_Count')

# Create a new data frame with total state counts from file
counts_total = data.groupby(['State']).size().reset_index(name='State_Count')

print(counts_total.head())

# create figure
fig = px.choropleth(counts_total, locations='State', locationmode="USA-states", color='State_Count', scope="usa")

fig.show()
