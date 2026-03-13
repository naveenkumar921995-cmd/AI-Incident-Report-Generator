def predict_severity(root_cause):

    severity_map = {

        "Poor housekeeping": 2,
        "Improper tool usage": 3,
        "Inadequate workplace lighting": 2,
        "PPE violation": 4,
        "Equipment failure": 4,
        "Unsafe act": 3

    }

    return severity_map.get(root_cause, 2)
