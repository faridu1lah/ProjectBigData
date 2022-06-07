import string
import streamlit as st
import pandas as pd
from db import connection


def load_view():

    st.markdown("## Predicting house prices in Amsterdam")
    # with st.form(key="my_form"):

    c1, c2 = st.columns([1, 5])

    with c1:

        # Title
        st.markdown("#### 🏠 Future house details?")

        amsterdam_data = pd.read_sql("SELECT gebiedcodenaam FROM amsterdam GROUP BY gebiedcodenaam", con=connection)

        # House type
        neighbourhood = st.selectbox("Your new neighbourhood:", amsterdam_data)

        # House type
        house_type = st.selectbox("Type Of house:", ("All", "Housing associations", "Private rent", "Purchased house"))
        # st.write("You selected:", house_type)

        # number square meters
        number_m = st.number_input("Square meters:", step=1)
        # st.write("The current number is ", number_m)

        neighbourhood_data = connection.execute(
            f"SELECT FLOOR(SUM(VCRIMIN_I) / count(*)) AS 'crime', FLOOR(SUM(Aanbod_basisscholen + Culturele_voorzieningen)) AS 'facilities' FROM amsterdam WHERE gebiedcodenaam = '{neighbourhood}'"
        ).first()

        # Crime percentage
        crime = st.number_input("Average crime encounters:", value=int(neighbourhood_data.crime), disabled=True)
        # st.write("Crime: ", crime_percentage)

        # Crime percentage
        facilities = st.number_input("Amount of facilities:", value=int(neighbourhood_data.facilities), disabled=True)
        # st.write("Crime: ", facilities_per)

        submit_button = st.button(label="🏠 Predict House Price!")

        if submit_button == True:

            # predict()

            st.write("Your info: ", neighbourhood, house_type, number_m, crime, facilities)

    with c2:

        st.markdown("### Check out the prices!")

        amsterdam_data = pd.read_sql("SELECT * FROM amsterdam INNER JOIN geo_info ON (amsterdam.wijkcode = geo_info.wijkcode)", con=connection)

        st.map(amsterdam_data)

    if not submit_button:
        st.stop()


# def predict():

#     amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0", con=connection)
#     amsterdam_data = amsterdam_data.apply(lambda x: x.apply(lambda y: y.str.replace(",", ".") if type(y) == string else y))

#     prices = amsterdam_data["WOZ_per_M2"]
#     features = amsterdam_data.drop(["WOZ_per_M2", "index", "niveau", "niveaunaam", "wijkcode", "gebiedcodenaam"], axis=1)
#     features = features.apply(pd.to_numeric, errors="coerce")

#     # Import 'train_test_split'
#     from sklearn.model_selection import train_test_split

#     # Shuffle and split the data into training and testing subsets
#     X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state=42)
#     # start most important step: Counting the words
#     from sklearn.feature_extraction.text import CountVectorizer

#     cv = CountVectorizer(binary=False)
#     X_train_cv = cv.fit_transform(X_train)
#     X_test_cv = cv.transform(X_test)

#     # X_trainX = X_train.transpose()
#     st.write(f"Test: {X_train.head(5)}")
#     st.write(f"Test: {y_train.head(5)}")

#     reg = fit_model(X_train_cv, y_train)

#     st.write("Parameter 'max_depth' is {} for the optimal model.".format(reg.get_params()["max_depth"]))

#     st.write("Amsterdam housing dataset has {} data points with {} variables each.".format(*amsterdam_data.shape))


# from sklearn.metrics import r2_score


# def performance_metric(y_true, y_predict):

#     # Calculates and returns the performance score between
#     # true (y_true) and predicted (y_predict) values based on the metric chosen.

#     score = r2_score(y_true, y_predict)

#     # Return the score
#     return score


# # Import 'make_scorer', 'DecisionTreeRegressor', and 'GridSearchCV'
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import make_scorer
# from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import ShuffleSplit


# def fit_model(X, y):

#     # Performs grid search over the 'max_depth' parameter for a
#     # decision tree regressor trained on the input data [X, y].

#     # Create cross-validation sets from the training data
#     cv_sets = ShuffleSplit(n_splits=10, test_size=0.20, random_state=0)

#     # Create a decision tree regressor object0
#     regressor = DecisionTreeRegressor()

#     # Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
#     params = {"max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

#     # Transform 'performance_metric' into a scoring function using 'make_scorer'
#     scoring_fnc = make_scorer(performance_metric)

#     # Create the grid search cv object --> GridSearchCV()
#     grid = GridSearchCV(estimator=regressor, param_grid=params, cv=cv_sets, scoring=scoring_fnc)

#     # Fit the grid search object to the data to compute the optimal model
#     grid = grid.fit(X, y)

#     # Return the optimal model after fitting the data
#     return grid.best_estimator_
