from textwrap import wrap
from nbformat import write
import numpy


def load_view():
    import streamlit as st

    st.markdown("## Predicting house prices in Amsterdam")
    # with st.form(key="my_form"):

    c1, c2 = st.columns([1, 5])
    import pandas as pd
    from db import connection

    with c1:

        # Title
        st.markdown("#### 🏠 Future house details?")

        amsterdam_data = pd.read_sql("SELECT gebiedcodenaam FROM amsterdam GROUP BY gebiedcodenaam", con=connection)

        # House type
        neighbourhood = st.selectbox("Your new neighbourhood:", amsterdam_data)

        # House type
        house_type = st.selectbox("Type Of house:", ("All", "Housing associations", "Private rent", "Purchased house"))
        # st.write("You selected:", house_type)

        # number square meters
        number_m = st.number_input("Square meters:")
        # st.write("The current number is ", number_m)

        neighbourhood_data = connection.execute(
            f"SELECT FLOOR(SUM(VCRIMIN_I) / count(*)) AS 'crime', FLOOR(SUM(Aanbod_basisscholen + Culturele_voorzieningen)) AS 'facilities' FROM amsterdam WHERE gebiedcodenaam = '{neighbourhood}'"
        ).first()

        # Crime percentage
        crime = st.number_input("Average crime encounters:", value=int(neighbourhood_data.crime), disabled=True)
        # st.write("Crime: ", crime_percentage)

        # Crime percentage
        facilities = st.number_input("Amount of facilities:", value=int(neighbourhood_data.facilities), disabled=True)
        # st.write("Crime: ", facilities_per)

        submit_button = st.button(label="🏠 Predict House Price!")

        if submit_button == True:
            st.write("Your info: ", neighbourhood, house_type, number_m, crime, facilities)

    with c2:

        st.markdown("### Check out the prices!")

        amsterdam_data = pd.read_sql("SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode)", con=connection)

        st.map(amsterdam_data)

    # if not submit_button:
    #     st.stop()
