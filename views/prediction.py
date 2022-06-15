import streamlit as st
import pandas as pd
from db import connection
import pydeck as pdk


def load_view():

    st.title("Predicting house prices in Amsterdam")

    # with st.form(key="my_form"):

    c1, c2 = st.columns([1, 5])

    with c1:

        # Title
        st.markdown("#### 🏠 Future house details?")

        amsterdam_data = pd.read_sql("SELECT gebiedcodenaam FROM amsterdam GROUP BY gebiedcodenaam", con=connection)

        # neighbourhood
        neighbourhood = st.selectbox("Your new neighbourhood:", amsterdam_data)

        # House type
        house_type = st.selectbox("Type Of house:", ("All", "Housing associations", "Private rent", "Purchased house"))
        # st.write("You selected:", house_type)

        # number square meters
        number_m = st.number_input("Square meters:", step=1, value=60)
        # st.write("The current number is ", number_m)

        neighbourhood_data = connection.execute(
            f"SELECT *, FLOOR(SUM(VCRIMIN_I) / count(*)) AS 'crime', FLOOR(SUM(Aanbod_basisscholen + Culturele_voorzieningen)) AS 'facilities' FROM amsterdam WHERE gebiedcodenaam = '{neighbourhood}'"
        ).first()

        # Crime percentage
        crime = st.number_input("Average crime encounters:", value=int(neighbourhood_data.crime))
        # st.write("Crime: ", crime_percentage)

        # facilities amount
        facilities = st.number_input("Amount of facilities:", value=int(neighbourhood_data.facilities))
        # st.write("Crime: ", facilities_per)

        submit_button = st.button(label="🏠 Predict House Price!")

        # if submit_button == True:
        #     st.write("Your info: ", neighbourhood, house_type, number_m, crime, facilities)

    with c2:

        st.markdown("### Check out the prices!")

        if submit_button == True:

            if "last_price" not in st.session_state:
                st.session_state["last_price"] = 0

            pre = predict(neighbourhood, house_type, number_m, crime, facilities, neighbourhood_data)
            st.markdown(f"#### 🏠 Your new house will cost you about : ")
            price = round((pre[0] * number_m), 2)

            st.metric(label="", value=f"€ {price}", delta=(pre[0] - st.session_state["last_price"]))

            st.session_state["last_price"] = pre[0]

        amsterdam_data = pd.read_sql("SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode)", con=connection)

        # st.map(amsterdam_data)

        # amsterdam_data

        st.pydeck_chart(
            pdk.Deck(
                # map_style="mapbox://styles/mapbox/light-v9",
                map_style="mapbox://styles/mapbox/navigation-day-v1",
                # initial_view_state=pdk.ViewState( latitude=4.89021995, longitude=-52.3837291 , zoom=11, pitch=50, ),
                initial_view_state=pdk.ViewState(
                    longitude=4.897070,
                    latitude=52.377956,
                    zoom=10.3,
                    pitch=50,
                ),
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=amsterdam_data,
                        get_position="[lon, lat]",
                        radius=500,
                        width_scale=20,
                        auto_highlight=True,
                        elevation_scale=2,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                        wireframe=True,
                        coverage=1,
                        # "PolygonLayer",
                        # data=amsterdam_data,
                        # id="geojson",
                        # opacity=0.8,
                        # stroked=False,
                        # get_polygon="coordinates",
                        # filled=True,
                        # extruded=True,
                        # wireframe=True,
                        # getWidth=0.01,
                        # getLineWidth=0.01,
                        # get_elevation="WOZ_per_M2",
                        # get_fill_color="WOZ_per_M2",
                        # get_line_color=[255, 255, 255],
                        # auto_highlight=True,
                        # pickable=True,
                    ),
                    # pdk.Layer(
                    #     "ScatterplotLayer",
                    #     data=amsterdam_data,
                    #     get_position="[lon, lat]",
                    #     get_color="[200, 30, 0, 160]",
                    #     get_radius=200,
                    # ),
                ],
                tooltip={
                    "html": "Elevation Value: {WOZ_per_M2}",
                    # "style": {
                    #     "backgroundColor": "gray",
                    #     "color": "white",
                    # },
                },
            )
        )

        # test = amsterdam_data["WOZ_per_M2"]
        # print(test)
        # st.markdown("test")

    if not submit_button:
        st.stop()


def predict(neighbourhood, house_type, number_m, crime, facilities, neighbourhood_data):
    from model import loadModel
    import pandas as pd

    client_data = {
        "Corporatiewoningen": [100 if house_type == "Housing associations" or house_type == "All" else 0],
        "Koopwoninging": [100 if house_type == "Purchased house" or house_type == "All" else 0],
        "Particuliere_huur": [100 if house_type == "Private rent" or house_type == "All" else 0],
        "gebiedscode": [connection.execute(f"SELECT gebiedscode FROM amsterdam WHERE gebiedcodenaam = '{neighbourhood}'").first().gebiedscode],
        "VCRIMIN_I": [crime],
        "Woningdichtheid": [neighbourhood_data.Woningdichtheid],
        "Culturele_voorzieningen": [facilities],
        "Aanbod_basisscholen": [facilities],
        "Woonoppervlak_0_40": [100 if (number_m >= 0 and number_m < 40) else 0],
        "Woonoppervlak_40_60": [100 if (number_m >= 40 and number_m < 60) else 0],
        "Woonoppervlak_60_80": [100 if (number_m >= 60 and number_m < 80) else 0],
        "Woonoppervlak_80_100": [100 if (number_m >= 80 and number_m < 100) else 0],
        "Woonoppervlak_100_plus": [100 if (number_m >= 100) else 0],
    }

    data = pd.DataFrame(client_data)

    # st.write(data)

    model = loadModel()
    pred = model.predict(data)

    return pred
