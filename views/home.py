from requests import head
from sqlalchemy import values


def load_view():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    st.title(f"Welcome by house prediction!")

    st.markdown("### WOZ value per square meters in neighbourhood(s)")

    # Reading all data
    from db import connection

    neighbourhood_data = pd.read_sql("SELECT gebiedcodenaam FROM amsterdam GROUP BY gebiedcodenaam", con=connection)

    # neighbourhood
    neighbourhood = st.multiselect(
        "Select a neighbourhood:",
        neighbourhood_data,
        [
            "AA Haarlemmerbuurt",
            "AB Jordaan",
            "AE Burgwallen-Oude Zijde",
            "AD Burgwallen-Nieuwe Zijde",
        ],
    )
    neighbourhoods = "','".join(neighbourhood)

    sql = f"SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0 AND gebiedcodenaam IN ('{neighbourhoods}')"

    amsterdam_data = pd.read_sql(sql, con=connection)
    amsterdam_data = amsterdam_data.rename(
        columns={
            "WOZ_per_M2": "WOZ value per square meters",
            "jaar": "Year",
            "wijkcode": "Neighbourhood code",
            "VCRIMIN_I": "Crime",
            "gebiedcodenaam": "Neighbourhood name",
        }
    )

    fig = px.scatter(
        amsterdam_data,
        x="Year",
        y="WOZ value per square meters",
        color="Woningdichtheid",
        size="WOZ value per square meters",
        hover_data=["Neighbourhood name"],
        color_continuous_scale='Bluered'
    )

    st.plotly_chart(fig, use_container_width=True)
    from model import getData, model_complexity, model_learning

    data = getData()
    chart1, chart2 = st.columns(2)

    chart1.pyplot(model_learning(data["X"], data["y"]), use_container_width=True)
    chart2.pyplot(model_complexity(data["X"], data["y"]), use_container_width=True)

    # charts
    woz = pd.read_excel("data/2021_jaarboek_stadsdeel_wozwaarde.xlsx")

    # Dropping unnecessary columns for bar charts
    wozPerArea = woz.drop(["gemiddelde WOZ-waarde per m2"], axis=1)
    wozPerAreaPerM2 = woz.drop(["gemiddelde WOZ-waarde"], axis=1)

    # Sorting values from high to low
    wozPerArea = wozPerArea.sort_values(by=wozPerArea.columns[1], ascending=False)
    wozPerAreaPerM2 = wozPerAreaPerM2.sort_values(by=wozPerAreaPerM2.columns[1], ascending=False)

    # Creating a bar chart for average per area
    avgPricePerArea = px.bar(
        wozPerArea,
        x=wozPerArea.columns[0],
        y=wozPerArea.columns[1],
        title="<b>Gemiddelde WOZ-waarde per gebied</b>",
        template="plotly_white",
    )

    # Creating a bar chart for average per are per M^2
    avgPricePerAreaPerM2 = px.bar(
        wozPerAreaPerM2,
        x=wozPerAreaPerM2.columns[0],
        y=wozPerAreaPerM2.columns[1],
        title="<b>Gemiddelde WOZ-waarde per gebied per vierkante meter</b>",
        template="plotly_white",
    )

    # Creating 2 columns
    col1, col2 = st.columns(2)

    # Placing both bar charts in 2 columns respectively
    col1.plotly_chart(avgPricePerArea, use_container_width=True)
    col2.plotly_chart(avgPricePerAreaPerM2, use_container_width=True)
