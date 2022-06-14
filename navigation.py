from views import home, prediction, contact
import streamlit as st


def load():

    checkDatabase()

    selected = navbar()

    if selected == "Home":

        home.load_view()

    if selected == "Prediction":

        prediction.load_view()

    if selected == "Contact":

        contact.load_view()


def navbar():
    from streamlit_option_menu import option_menu

    return option_menu(
        menu_title="House",  # required
        options=["Home", "Prediction", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="house",  # optional
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0 !important",
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
                "padding-left": "2px",
                "padding-right": "2px",
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


def mob_navbar():
    from streamlit_option_menu import option_menu

    return option_menu(
        menu_title="House",  # required
        options=["Home", "Prediction", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="house",  # optional
        styles={
            "icon": {"color": "#44A1B5", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
            },
            "nav-link-selected": {"background-color": "#073045"},
            "menu-title": {"margin": "0 2em", "align-self": "center", "font-weight": "bolder", "color": "#44A1B5", "white-space": "nowrap"},
        },
    )


def checkDatabase():

    params = st.experimental_get_query_params()
    token = params["token"][0] if "token" in params else ""

    if token == "bestgroup":

        st.title("Updated database from csv!")

        from db import connection
        from cleaning import getData, getGeoInfo

        data = getData()
        latLonData = getGeoInfo()

        data.to_sql(name="amsterdam", con=connection, if_exists="replace", index=True, chunksize=1000)
        latLonData.to_sql(name="geo_info", con=connection, if_exists="replace", index=True, chunksize=1000)
