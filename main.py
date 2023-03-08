import pandas as pd
import folium
import webbrowser
import os
from geopy.geocoders import Nominatim

# Load COVID-19 data into a Pandas dataframe
df = pd.read_csv('WHO-COVID-19-global-data.csv')

# Create a Nominatim geolocator
geolocator = Nominatim(user_agent='my-app')

# Create a Folium map centered on the world
map = folium.Map(location=[0, 0], zoom_start=2)

# Loop through each country in the dataframe
for country in df['Country'].unique():

    # Get the latitude and longitude coordinates of the country
    location = geolocator.geocode(country)

    # Skip over countries that do not have a valid location
    if location is None:
        continue

    # Get the number of COVID-19 cases for the country
    cases = df.loc[df['Country'] == country, 'Cumulative_cases'].max()

    # Add a circle marker to the map for the country, with size and color based on the number of cases
    folium.CircleMarker(location=[location.latitude, location.longitude],
                        radius=cases/100000,
                        color='red',
                        fill_color='red',
                        fill_opacity=0.5,
                        popup=f"{country}: {cases} cases").add_to(map)

# Display the map
# Save the map as an HTML file
map.save('covid_map.html')

# Open the map in a new window

webbrowser.open('file://' + os.path.realpath('covid_map.html'))