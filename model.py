def create_model():

    import pandas as pd
    from db import connection

    amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0", con=connection)

    features = [
        "Corporatiewoningen",
        "Koopwoninging",
        "Particuliere_huur",
        "gebiedscode",
        "VCRIMIN_I",
        "Woningdichtheid",
        "Culturele_voorzieningen",
        "Aanbod_basisscholen",
        "Woonoppervlak_0_40",
        "Woonoppervlak_40_60",
        "Woonoppervlak_60_80",
        "Woonoppervlak_80_100",
        "Woonoppervlak_100_plus",
    ]

    y = amsterdam_data["WOZ_per_M2"]
    X = amsterdam_data[features]

    from sklearn.model_selection import train_test_split

    # splitting the data, no crossfold validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    reg = fit_model(X_train, y_train)

    saveModel(reg)

    model = loadModel()

    p = model.predict(X_test)
    print(p)

    print("Parameter 'max_depth' is {} for the optimal model.".format(model.get_params()["max_depth"]))

    print("Amsterdam housing dataset has {} data points with {} variables each.".format(*amsterdam_data.shape))


def performance_metric(y_true, y_predict):

    # Calculates and returns the performance score between
    # true (y_true) and predicted (y_predict) values based on the metric chosen.
    from sklearn.metrics import r2_score

    score = r2_score(y_true, y_predict)

    # Return the score
    return score


def fit_model(X, y):
    # Performs grid search over the 'max_depth' parameter for a
    # decision tree regressor trained on the input data [X, y].

    # Import 'make_scorer', 'DecisionTreeRegressor', and 'GridSearchCV'
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import make_scorer
    from sklearn.model_selection import GridSearchCV, ShuffleSplit

    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(n_splits=10, test_size=0.20, random_state=0)

    # Create a decision tree regressor object
    regressor = DecisionTreeRegressor()

    # Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
    params = {"max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

    # Transform 'performance_metric' into a scoring function using 'make_scorer'
    scoring_fnc = make_scorer(performance_metric)

    # Create the grid search cv object --> GridSearchCV()
    # Make sure to include the right parameters in the object:
    # (estimator, param_grid, scoring, cv) which have values 'regressor', 'params', 'scoring_fnc', and 'cv_sets' respectively.
    grid = GridSearchCV(estimator=regressor, param_grid=params, scoring=scoring_fnc, cv=cv_sets)

    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)

    # Return the optimal model after fitting the data
    return grid.best_estimator_


def saveModel(model):
    import pickle

    pickle.dump(model, open("pickle_model.sav", "wb"))


def loadModel():
    import pickle

    try:
        return pickle.load(open("pickle_model.sav", "rb"))
    except (OSError, IOError) as e:
        return False


def getData():
    from db import connection
    import pandas as pd

    amsterdam_data = pd.read_sql("SELECT * FROM amsterdam WHERE WOZ_per_M2 > 0", con=connection)

    features = [
        "Corporatiewoningen",
        "jaar",
        "Koopwoninging",
        "Particuliere_huur",
        "gebiedscode",
        "VCRIMIN_I",
        "Woningdichtheid",
        "Culturele_voorzieningen",
        "Aanbod_basisscholen",
        "Woonoppervlak_0_40",
        "Woonoppervlak_40_60",
        "Woonoppervlak_60_80",
        "Woonoppervlak_80_100",
        "Woonoppervlak_100_plus",
    ]

    y = amsterdam_data["WOZ_per_M2"]
    X = amsterdam_data[features]

    return {"X": X, "y": y}


import matplotlib.pyplot as pl
import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import ShuffleSplit

# visual
def model_complexity(X, y):

    # Calculates the performance of the model as model complexity increases.
    # The learning and testing errors rates are then plotted.

    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.5, random_state=0)

    # Vary the max_depth parameter from 1 to 10
    max_depth = np.arange(1, 11)

    # Calculate the training and testing scores
    train_scores, test_scores = validation_curve(DecisionTreeRegressor(), X, y, param_name="max_depth", param_range=max_depth, cv=cv, scoring="r2")

    # Find the mean and standard deviation for smoothing
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Plot the validation curve
    pl.style.use("seaborn")

    pl.figure(figsize=(7, 3))
    pl.title("Decision Tree Regressor Complexity Performance")
    pl.plot(max_depth, train_mean, "o-", color="r", label="Training Score")
    pl.plot(max_depth, test_mean, "o-", color="g", label="Validation Score")
    pl.fill_between(max_depth, train_mean - train_std, train_mean + train_std, alpha=0.15, color="r")
    pl.fill_between(max_depth, test_mean - test_std, test_mean + test_std, alpha=0.15, color="g")

    # Visual aesthetics
    pl.legend(loc="lower right")
    pl.xlabel("Maximum Depth")
    pl.ylabel("Score")
    pl.ylim([-0.05, 1.05])
    # pl.show()

    return pl


def model_learning(X, y):
    # Calculates the performance of several models with varying sizes of training data.
    # The learning and testing scores for each model are then plotted.

    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

    # Generate the training set sizes increasing by 50
    train_sizes = np.rint(np.linspace(1, X.shape[0] * 0.8 - 1, 9)).astype(int)

    # Create the figure window
    pl.style.use("seaborn")

    fig = pl.figure(figsize=(10, 15))

    # Create three different models based on max_depth
    for k, depth in enumerate([1, 3, 6, 10]):

        # Create a Decision tree regressor at max_depth = depth
        regressor = DecisionTreeRegressor(max_depth=depth)

        # Calculate the training and testing scores
        sizes, train_scores, test_scores = learning_curve(regressor, X, y, cv=cv, train_sizes=train_sizes, scoring="r2")

        # Find the mean and standard deviation for smoothing
        train_std = np.std(train_scores, axis=1)
        train_mean = np.mean(train_scores, axis=1)
        test_std = np.std(test_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)

        # Subplot the learning curve
        ax = fig.add_subplot(4, 1, k + 1)
        ax.plot(sizes, train_mean, "o-", color="r", label="Training Score")
        ax.plot(sizes, test_mean, "o-", color="g", label="Testing Score")
        ax.fill_between(sizes, train_mean - train_std, train_mean + train_std, alpha=0.15, color="r")
        ax.fill_between(sizes, test_mean - test_std, test_mean + test_std, alpha=0.15, color="g")

        # Labels
        ax.set_title("max_depth = %s" % (depth))
        ax.set_xlabel("Number of Training Points")
        ax.set_ylabel("Score")
        ax.set_xlim([0, X.shape[0] * 0.8])
        ax.set_ylim([-0.05, 1.05])
        ax.legend(borderaxespad=0.0)

    # Visual aesthetics
    fig.suptitle("Decision Tree Regressor Learning Performances", fontsize=14, y=1)
    fig.tight_layout()
    # fig.show()

    return fig


# models = {"Regression": linear_model.LinearRegression, "Decision Tree": tree.DecisionTreeRegressor, "k-NN": neighbors.KNeighborsRegressor}


def display_plot(X, y):
    import plotly.graph_objects as go

    # df = px.data.tips()  # replace with your own data source
    # X = df.total_bill.values[:, None]
    # X_train, X_test, y_train, y_test = train_test_split(X, df.tip, random_state=42)

    model = loadModel()

    import streamlit as st

    st.write(str(X.min().apply(lambda x: float(x)).sum()))

    # x_range = np.linspace(X.min().apply(lambda x: float(x)).sum(), X.max().apply(lambda x: float(x)).sum(), 100)

    # y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure(
        [
            go.Scatter(x=X["jaar"], y=y, name="actual", mode="markers", color=""),
            # go.Scatter(x=X_test.squeeze(), y=y_test, name="test", mode="markers"),
            # go.Scatter(x=x_range, y=y_range, name="prediction"),
        ]
    )

    return fig
