import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_incident_trend(data):

    monthly_counts = data.groupby("month").size().reset_index(name="incidents")

    X = np.arange(len(monthly_counts)).reshape(-1,1)
    y = monthly_counts["incidents"]

    model = LinearRegression()
    model.fit(X,y)

    future = model.predict([[len(monthly_counts)]])

    return int(future[0])
