def predict_severity(risk_score):

    if risk_score <= 4:
        return "Minor"

    elif risk_score <= 9:
        return "Moderate"

    elif risk_score <= 16:
        return "Major"

    else:
        return "Critical"
