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

import pandas as pd
from db import connection
import string

amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0", con=connection)
# amsterdam_data = amsterdam_data.drop(["index", "niveau", "niveaunaam", "wijkcode", "gebiedcodenaam"], axis=1)
amsterdam_data = amsterdam_data.drop(["index"], axis=1)


Stock_Market = {
    "Year": [
        2017,
        2016,
    ],
    "Month": [
        12,
        11,
    ],
    "Interest_Rate": [
        2.75,
        2.5,
    ],
    "Unemployment_Rate": [
        5.3,
        4.3,
    ],
    "Stock_Index_Price": [
        1464,
        1394,
    ],
}

# amsterdam_data = amsterdam_data.apply(lambda x: x.apply(lambda y: float(y.str.replace(",", ".")) if type(y) == "" else y))
# amsterdam_data.head(5)


# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()
# amsterdam_data[amsterdam_data.columns] = amsterdam_data[amsterdam_data.columns].apply(le.fit_transform)

# amsterdam_data.head()
df = pd.DataFrame(Stock_Market, columns=["Year", "Month", "Interest_Rate", "Unemployment_Rate", "Stock_Index_Price"])

y = df["Stock_Index_Price"]
X = df[["Interest_Rate", "Unemployment_Rate"]]


# X = X.transpose()
# X = X.reshape(X.shape[1:])

# X.shape
# y.shape


# from sklearn.utils.validation import check_consistent_length

# # print(check_consistent_length(prices, [features]))

# X.head()

from sklearn.model_selection import train_test_split

# splitting the data, no crossfold validation
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)

from sklearn.feature_extraction.text import CountVectorizer

# cv = CountVectorizer(binary=False)
# X_train_cv = cv.fit_transform(X_train)
# X_test_cv = cv.transform(X_test)

# from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

# logreg_model = LogisticRegression(C=1.0, max_iter=100)
logreg_model = LinearRegression()
logreg_model.fit(X_train, y_train)

prediction = logreg_model.predict(X_test)
print(prediction)
