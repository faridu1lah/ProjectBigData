from datetime import date
from operator import index
import streamlit as st
import pandas as pd
from db import connection
import pydeck as pdk


def load_view():

    st.title("Predicting house prices in Amsterdam")

    # with st.form(key="my_form"):

    c1, c2, c3 = st.columns([1, 2, 3])

    with c1:

        # Title
        st.markdown("#### 🏠 Future house details?")

        amsterdam_data = pd.read_sql("SELECT gebiedcodenaam FROM amsterdam GROUP BY gebiedcodenaam", con=connection)

        # neighbourhood
        neighbourhood = st.selectbox("Your new neighbourhood:", amsterdam_data)

        neighbourhood_data = connection.execute(f"SELECT * FROM big_data.amsterdam WHERE gebiedcodenaam = '{neighbourhood}'").first()

        # number square meters
        number_m = st.number_input("Square meters:", step=1, value=60)
        percentage_0_40 = st.number_input("Percentage tussen de 0 en 40 m2:", step=1, value=int(neighbourhood_data.Woonoppervlak_0_40))
        percentage_40_60 = st.number_input("Percentage tussen de 40 en 60 m2:", step=1, value=int(neighbourhood_data.Woonoppervlak_40_60))
        percentage_60_80 = st.number_input("Percentage tussen de 60 en 80 m2:", step=1, value=int(neighbourhood_data.Woonoppervlak_60_80))
        percentage_80_100 = st.number_input("Percentage tussen de 80 en 100 m2:", step=1, value=int(neighbourhood_data.Woonoppervlak_80_100))
        percentage_100plus = st.number_input("Percentage 100 plus m2:", step=1, value=int(neighbourhood_data.Woonoppervlak_100_plus))
        percentage_corporatie = st.number_input("Percentage corperatie woningen:", step=1, value=int(neighbourhood_data.Corporatiewoningen))
        percentage_koop = st.number_input("Percentage koop woningen:", step=1, value=int(neighbourhood_data.Koopwoninging))
        percentage_particulier = st.number_input("Percentage particuliere huurwoningen:", step=1, value=int(neighbourhood_data.Particuliere_huur))
        woningdichtheid = st.number_input("Woningdichtheid:", step=1, value=int(neighbourhood_data.Woningdichtheid))
        WOZ_waarde = neighbourhood_data.WOZ_per_M2
        submit_button = st.button(label="🏠 Predict House Price!")

        # if submit_button == True:
        #     st.write("Your info: ", neighbourhood, house_type, number_m, crime, facilities)

    with c2:

        st.markdown("### Check out the price!")

        if submit_button == True:

            if "last_price" not in st.session_state:
                st.session_state["last_price"] = 0

            pre = predict(
                neighbourhood,
                percentage_0_40,
                percentage_40_60,
                percentage_60_80,
                percentage_80_100,
                percentage_100plus,
                percentage_corporatie,
                percentage_koop,
                percentage_particulier,
                WOZ_waarde,
                woningdichtheid,
            )
            price = round((pre[0] * number_m), 2)

            st.markdown("#### 🏠 Your new house will cost you about:")

            st.metric(label="", value=f"€ {price}", delta=(pre[0] - st.session_state["last_price"]))

            st.session_state["last_price"] = pre[0]

        from model import display_plot, get_data

        data = get_data()

        c2.plotly_chart(display_plot(data["X"], data["y"]), use_container_width=True)

    with c3:

        st.markdown("### Check out the Neighbourhood!")

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
                    ),
                ],
            )
        )

    if not submit_button:
        st.stop()


def predict(
    neighbourhood,
    percentage_0_40,
    percentage_40_60,
    percentage_60_80,
    percentage_80_100,
    percentage_100plus,
    percentage_corporatie,
    percentage_koop,
    percentage_particulier,
    WOZ_waarde,
    woningdichtheid,
):
    from model import load_model
    import pandas as pd
    from datetime import date

    client_data = {
        "jaar": [date.today().year],
        "WWOZ_PREV1": [WOZ_waarde],
        "Corporatiewoningen": [percentage_corporatie],
        "Koopwoninging": [percentage_koop],
        "Particuliere_huur": [percentage_particulier],
        "gebiedscode": [connection.execute(f"SELECT gebiedscode FROM amsterdam WHERE gebiedcodenaam = '{neighbourhood}'").first().gebiedscode],
        "Woningdichtheid": [woningdichtheid],
        "Woonoppervlak_0_40": [percentage_0_40],
        "Woonoppervlak_40_60": [percentage_40_60],
        "Woonoppervlak_60_80": [percentage_60_80],
        "Woonoppervlak_80_100": [percentage_80_100],
        "Woonoppervlak_100_plus": [percentage_100plus],
    }

    df = pd.DataFrame(data=client_data)

    # st.write(data)

    model = load_model()
    pred = model.predict(df)

    return pred
