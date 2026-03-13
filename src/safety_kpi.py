import pandas as pd

def calculate_kpis(data):

    total_incidents = len(data)

    near_miss = len(data[data["root_cause"] == "Near Miss"])

    unsafe_conditions = len(data[data["root_cause"] == "Unsafe Condition"])

    closure_rate = round((unsafe_conditions / total_incidents) * 100, 2)

    training_compliance = 85
    ppe_compliance = 90

    return {
        "Total Incidents": total_incidents,
        "Near Miss Reports": near_miss,
        "Unsafe Condition Reports": unsafe_conditions,
        "Closure Rate (%)": closure_rate,
        "Training Compliance (%)": training_compliance,
        "PPE Compliance (%)": ppe_compliance
    }
