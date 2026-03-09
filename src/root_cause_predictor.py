import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "incidents_dataset.csv")

data = pd.read_csv(data_path)

X = data["incident"]
y = data["root_cause"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = RandomForestClassifier()
model.fit(X_vec, y)

def predict_root_cause(description):

    X_input = vectorizer.transform([description])
    prediction = model.predict(X_input)

    return prediction[0]
