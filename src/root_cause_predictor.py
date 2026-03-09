import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def predict_root_cause(description):

    # dataset path
    data_path = os.path.join(BASE_DIR, "data", "incidents_dataset.csv")

    # load dataset
    data = pd.read_csv(data_path)

    X = data["incident"]
    y = data["root_cause"]

    # train model
    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = RandomForestClassifier()
    model.fit(X_vec, y)

    # prediction
    X_input = vectorizer.transform([description])
    prediction = model.predict(X_input)

    return prediction[0]
