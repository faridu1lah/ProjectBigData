import imp
from pandas import DataFrame
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
        .css-1cpxqw2{ width:100% !important;}
    </style> """,
    unsafe_allow_html=True,
)

# load navigation options and content
navigation.load()


# testen

# from model import loadModel
# import pandas as pd

# model = loadModel()

# # client_data = {"gebiedscode": [0], "Woonoppervlak_0_40": [2], "VCRIMIN_I": [2]}

# # data = pd.DataFrame(client_data)
# # data.head()

# client_data = {
#     "Corporatiewoningen": [1],
#     "Koopwoninging": [0],
#     "Particuliere_huur": [0],
#     "gebiedscode": [0],
#     "VCRIMIN_I": [1],
#     "Woningdichtheid": [1],
#     "Culturele_voorzieningen": [1],
#     "Aanbod_basisscholen": [1],
#     "Woonoppervlak_0_40": [0],
#     "Woonoppervlak_40_60": [1],
#     "Woonoppervlak_60_80": [0],
#     "Woonoppervlak_80_100": [0],
#     "Woonoppervlak_100_plus": [0],
# }

# data = pd.DataFrame(client_data)

# pred = model.predict(data)
# print(pred)

# import pandas as pd

# data = {"A": ["10,3", "3,3", "10,4"]}
# df = pd.DataFrame(data)

# df = df.apply(lambda x: x.str.replace(",", "."))

# df["A"] = df["A"].astype(float)

# st.write("Your info: ", df.to_string())


# import pandas as pd
# from db import connection
# import plotly.express as px

# amsterdam_data = pd.read_sql(
#     "SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode) WHERE WOZ_per_M2 IS NOT NULL", con=connection
# )

# amsterdam_data.to_csv("tableu.csv")


# dit is voor testen
# amsterdam_data = amsterdam_data.apply(lambda x: x.apply(lambda y: float(y.str.replace(",", ".")) if type(y) == "" else y))
# amsterdam_data.head(5)


# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# amsterdam_data[amsterdam_data.columns] = amsterdam_data[amsterdam_data.columns].apply(le.fit_transform)

# # amsterdam_data.head()
# df = pd.DataFrame(Stock_Market, columns=["Year", "Month", "Interest_Rate", "Unemployment_Rate", "Stock_Index_Price"])

# y = df["Stock_Index_Price"]
# X = df[["Interest_Rate", "Unemployment_Rate"]]

# import pandas as pd
# from db import connection

# amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0 LIMIT 50", con=connection)

# features = [
#     "Corporatiewoningen",
#     "Koopwoninging",
#     "Particuliere_huur",
#     "WOZ_per_M2",
#     "gebiedscode",
#     "VCRIMIN_I",
#     "Woningdichtheid",
#     "Culturele_voorzieningen",
#     "Aanbod_basisscholen",
#     "Woonoppervlak_0_40",
#     "Woonoppervlak_40_60",
#     "Woonoppervlak_60_80",
#     "Woonoppervlak_80_100",
#     "Woonoppervlak_100_plus",
# ]

# y = amsterdam_data["WOZ_per_M2"]
# X = amsterdam_data[features]

# from sklearn.model_selection import train_test_split

# # splitting the data, no crossfold validation
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# from sklearn.linear_model import LinearRegression

# model = LinearRegression()
# model.fit(X_train, y_train)

# # model.fit_transform(y_test, y_test)


# client_data = {"gebiedscode": [0], "Woonoppervlak_0_40": [2], "VCRIMIN_I": [2]}
# data = pd.DataFrame(client_data)
# data.head()

# prediction = model.predict(data)

# print(prediction)
