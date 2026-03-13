def calculate_risk(root_cause):

    risk_table = {

        "Poor housekeeping": {
            "likelihood": 4,
            "severity": 3
        },

        "Improper tool usage": {
            "likelihood": 3,
            "severity": 4
        },

        "Inadequate workplace lighting": {
            "likelihood": 3,
            "severity": 3
        },

        "Unsafe work practice": {
            "likelihood": 4,
            "severity": 4
        }

    }

    risk = risk_table.get(root_cause, {"likelihood":2,"severity":2})

    likelihood = risk["likelihood"]
    severity = risk["severity"]

    risk_score = likelihood * severity

    return likelihood, severity, risk_score
