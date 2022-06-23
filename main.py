import streamlit as st
import navigation

# setup tab title
st.set_page_config(page_title="Big Data", layout="wide")

# add css to document
st.markdown(
    """ 
    <style>
         a, a:hover, a:link, a:visited{ all: unset;}
        .block-container {padding-bottom:1rem; }
        .main iframe[title="streamlit_option_menu.option_menu"] {position:fixed; top:0;right: 0;left: 0;width: 100%;z-index:9999999;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .css-1cpxqw2{ width:100% !important;}
        .custom_button{
            width:100% !important;
            display: inline-flex;
            -webkit-box-align: center;
            align-items: center;
            -webkit-box-pack: center;
            justify-content: center;
            font-weight: 400;
            padding: 0.25rem 0.75rem;
            border-radius: 0.25rem;
            margin: 0px;
            line-height: 1.6;
            color: inherit;
            width: auto;
            user-select: none;
            background-color: rgb(255, 255, 255);
            border: 1px solid rgba(49, 51, 63, 0.2);
        }
        .custom_button:hover{border-color: rgb(255, 75, 75);color: rgb(255, 75, 75);}
    </style> """,
    unsafe_allow_html=True,
)

# load navigation options and content
navigation.load()

from model import create_model

create_model()
