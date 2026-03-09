import joblib

model = joblib.load("models/root_cause_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_root_cause(description):

    X = vectorizer.transform([description])
    prediction = model.predict(X)

    return prediction[0]
