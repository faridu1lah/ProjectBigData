import imp
import streamlit as st
import navigation

# setup broweser tab title
st.set_page_config(page_title="Big Data", layout="wide")

# add css to document
st.markdown(
    """ 
    <style>
        .block-container {padding-bottom:1rem; }
        iframe[title="streamlit_option_menu.option_menu"] {position:fixed; top:0;right: 0;left: 0;width: 100%;z-index:9999999;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style> """,
    unsafe_allow_html=True,
)

# load navigation options and content
navigation.load()
