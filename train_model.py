import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/incidents_dataset.csv")

X = data["incident"]
y = data["root_cause"]

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = RandomForestClassifier()
model.fit(X_vec, y)

joblib.dump(model, "models/root_cause_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained and saved.")
