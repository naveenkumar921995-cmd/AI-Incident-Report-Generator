import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def predict_root_cause(description):

    model_path = os.path.join(BASE_DIR, "models", "root_cause_model.pkl")
    vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    X = vectorizer.transform([description])
    prediction = model.predict(X)

    return prediction[0]
