def load_view():
    import streamlit as st

    st.markdown("## Predicting house prices in Amsterdam")
    with st.form(key="my_form"):

        c1, c2 = st.columns([1, 5])

        with c1:

            # Title
            st.markdown("#### 🏠 Future house details?")

            # House type
            house_type = st.selectbox("Type Of house:", ("All", "Housing associations", "Private rent", "Purchased house"))
            # st.write("You selected:", house_type)

            # number square meters
            number_m = st.number_input("Square meters:")
            # st.write("The current number is ", number_m)

            # Crime percentage
            crime_per = st.slider("Crime percentage:", 0, 100, 25)
            # st.write("Crime: ", crime_percentage)

            # Crime percentage
            facilities_per = st.slider("Facilities percentage:", 0, 100, 25)
            # st.write("Crime: ", facilities_per)

            submit_button = st.form_submit_button(label="🏠 Predict House Price!")

            if submit_button == True:
                st.write("Your info: ", house_type, number_m, crime_per, facilities_per)

        with c2:

            st.markdown("### Check out the prices!")

            import pandas as pd
            from db import connection

            amsterdam_data = pd.read_sql("SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode)", con=connection)

            st.map(amsterdam_data)

    if not submit_button:
        st.stop()
