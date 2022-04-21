from numpy import nanvar
#from db import connection
import streamlit as sl
import pandas as pd
#import folium
import navbar as nav

# if connection.is_connected():
#     cursor = connection.cursor()
#     cursor.execute("select database();")
#     print("You're connected to database in main: ", cursor.fetchone())


header = sl.container()
dataset = sl.container()
# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1
amsterdam_data = pd.read_csv("data/h-amsterdam.csv")
map_data = amsterdam_data

# with header:
#     sl.title("Hallo Big Data")
selected = nav.streamlit_menu(example=EXAMPLE_NO)
selected1= nav.streamlit_menu(example=2)
selected2 = nav.streamlit_menu(example=3)

if selected == "Home":
    sl.title(f"You have selected {selected}")
    map_data.rename(columns={"Lat": "lat", "Lon": "lon"}, inplace=True)

    sl.map(map_data)
if selected == "Projects":
    sl.title(f"You have selected {selected1}")
    ch_data = amsterdam_data
# ch_data["PriceRoom"] = ch_data["Price"] / 100 / ch_data["Room"]

    chart_data = pd.DataFrame(amsterdam_data, columns=["Price", "Room"])

    sl.line_chart(chart_data)

if selected == "Contact":
    sl.title(f"You have selected {selected2}")



with dataset:
    sl.write(amsterdam_data.head(100))


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
