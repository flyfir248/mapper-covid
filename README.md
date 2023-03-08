## COVID-19 Mapper

This is a Python script that uses the geopy and folium libraries to create an interactive map of COVID-19 cases around the world. The map highlights each country with a red circle marker whose size and opacity is proportional to the number of COVID-19 cases in that country.

Installation
To use this script, you will need to have the following libraries installed:

+ Pandas 
+ Folium 
+ Geopy

You can install these libraries using pip:
```
pip install pandas folium geopy
```

### Usage
To use the script, follow these steps:

+ Download the COVID-19-data.csv file, which contains the COVID-19 case data, to the same directory as the script.
+ Open a terminal or command prompt and navigate to the directory containing the script.
+ Run the script using the following command:

```
python covid_mapper.py
```

+ The script will generate an HTML file called covid_map.html, which will display the interactive map in your default web browser.

## Customization
You can customize the appearance of the map by modifying the following lines of code in the covid_mapper.py script:

* zoom_start: Set the initial zoom level of the map.
* radius: Set the base radius of the circle markers.
* fill_opacity: Set the opacity of the circle markers.
* fill_color: Set the fill color of the circle markers.
* color: Set the border color of the circle markers.

You can also modify the popup information displayed when a circle marker is clicked by modifying the popup parameter in the CircleMarker function.