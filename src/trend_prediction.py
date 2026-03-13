import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_trend(data):

    data["index"] = range(len(data))

    X = data[["index"]]
    y = data["incident_count"]

    model = LinearRegression()
    model.fit(X, y)

    future_index = np.array([[len(data) + i] for i in range(6)])

    predictions = model.predict(future_index)

    return predictions
