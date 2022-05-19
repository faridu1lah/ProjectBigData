def load_view():
    import streamlit as st
    import pandas as pd
    import plotly.express as px

    st.title(f"Welcome by house prediction!")

    # Reading all data
    from db import connection

    amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 IS NOT NULL", con=connection)
    amsterdam_data = amsterdam_data.rename(
        columns={"WOZ_per_M2": "WOZ waarde per vierkante meter!", "jaar": "Jaar", "wijkcode": "Wijkcode", "gebiedcodenaam": "Gebiedcodenaam"}
    )

    fig = px.scatter(
        amsterdam_data,
        x="WOZ waarde per vierkante meter!",
        y="Wijkcode",
        color="Jaar",
        size="WOZ waarde per vierkante meter!",
        hover_data=["WOZ waarde per vierkante meter!", "Gebiedcodenaam"],
        title="WOZ waarde per vierkante meter per wijk",
    )

    st.plotly_chart(fig, use_container_width=True)

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
        wozPerArea, x=wozPerArea.columns[0], y=wozPerArea.columns[1], title="<b>Gemiddelde WOZ-waarde per gebied</b>", template="plotly_white"
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
    col1.plotly_chart(avgPricePerArea)
    col2.plotly_chart(avgPricePerAreaPerM2)
