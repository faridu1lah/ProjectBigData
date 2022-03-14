from db import connection
import streamlit as sl
import pandas as pd
import folium

if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("select database();")
    print("You're connected to database in main: ", cursor.fetchone())


header = sl.container()
dataset = sl.container()

with header:
    sl.title("Hallo Big Data")

amsterdam_data = pd.read_csv("data/h-amsterdam.csv")

with dataset:
    sl.write(amsterdam_data.head(100))

map_data = amsterdam_data
map_data.rename(columns={"Lat": "lat", "Lon": "lon"}, inplace=True)

sl.map(map_data)

# map = folium.Map(
#     location=[
#         map_data.lat.mean(),
#         map_data.lon.mean(),
#     ],
#     zoom_start=14,
#     control_scale=True,
# )

# m = folium.Map(
#     location=[45.523, -122.675],
#     zoom_start=2,
#     tiles="https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=mytoken",
#     attr="Mapbox attribution",
# )

# sl.write(m)


# map.Choropleth(name="test", data=map_data)
