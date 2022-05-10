def load():
    # 2. horizontal menu with custom style
    from streamlit_option_menu import option_menu
    import streamlit as st
    import pandas as pd

    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Prediction", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        orientation="horizontal",
        styles={
            "container": {"padding": "0 !important", "margin": "0", "max-width": "100%", "border-radius": "0"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-item": {
                "flex-grow": "unset",
                "flex-basis": "unset",
            },
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                # "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#073045"},
        },
    )

    if selected == "Home":
        # home.load_view()
        amsterdam_data = pd.read_csv("data/h-amsterdam.csv")
        map_data = amsterdam_data
        st.title(f"You have selected {selected}")
        map_data.rename(columns={"Lat": "lat", "Lon": "lon"}, inplace=True)

        st.map(map_data)

    if selected == "Prediction":

        from views import prediction

        prediction.load_view()

    if selected == "Contact":
        st.title(f"You have selected {selected}")
