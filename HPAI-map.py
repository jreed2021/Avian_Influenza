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

state_abbreviation = {
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States.
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming"
}

# convert a state name to the state abbreviation
def state_conversion(state):
    for abbreviation, name in state_abbreviation.items():
        if state == name:
            return(abbreviation)

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
