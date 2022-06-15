from views import home, info, prediction
import streamlit as st

# load view
def load():

    checkDatabase()

    selected = navbar()

    if selected == "Home":

        home.load_view()

    if selected == "Prediction":

        prediction.load_view()

    if selected == "Info":

        info.load_view()


# custom navbar
def navbar():
    from streamlit_option_menu import option_menu

    return option_menu(
        menu_title="House",  # required
        options=["Home", "Prediction", "Info"],  # required
        icons=["house", "book", "info-circle"],  # optional
        menu_icon="house",  # optional
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0 3px !important",
                "margin": "0",
                "max-width": "100%",
                "border-radius": "0",
                "place-content": "space-between",
                "flex-direction": "row !important",
            },
            "icon": {"color": "#44A1B5", "font-size": "1em", "margin-right": "1px"},
            "nav-item": {
                "flex-grow": "unset",
                "flex-basis": "unset",
            },
            "nav": {
                "margin": "0px !important",
                "place-content": "center",
            },
            "nav-link": {
                "font-size": "1em",
                "text-align": "left",
                "margin": "0px 1px",
                "padding-left": "3px",
                "padding-right": "3px",
            },
            "nav-link-selected": {"background-color": "#073045"},
            "menu-title": {
                "margin": "0",
                "align-self": "center",
                "font-weight": "bolder",
                "color": "#44A1B5",
                "white-space": "nowrap",
            },
        },
    )


# update database from csv
def checkDatabase():

    params = st.experimental_get_query_params()
    token = params["token"][0] if "token" in params else ""

    if token == "bestgroup":

        st.title("Updated database from csv!")

        from db import connection
        from cleaning import getData, getGeoInfo

        data = getData()
        latLonData = getGeoInfo()

        data.to_sql(name="amsterdam", con=connection, if_exists="replace", index=False, chunksize=1000)
        latLonData.to_sql(name="geo_info", con=connection, if_exists="replace", index=False, chunksize=1000)
