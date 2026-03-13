from datetime import datetime, timedelta

def generate_capa(root_cause):

    actions = {
        "Poor Housekeeping": {
            "corrective": "Clean affected area immediately and remove oil spill.",
            "preventive": "Implement daily housekeeping inspection checklist."
        },

        "Improper Tool Usage": {
            "corrective": "Stop unsafe work and inspect tools.",
            "preventive": "Conduct tool usage training for workers."
        },

        "Inadequate Lighting": {
            "corrective": "Install temporary lighting immediately.",
            "preventive": "Perform monthly lighting inspection."
        }
    }

    default_action = {
        "corrective": "Investigate issue and correct unsafe condition.",
        "preventive": "Implement safety training and monitoring."
    }

    action = actions.get(root_cause, default_action)

    return {
        "corrective": action["corrective"],
        "preventive": action["preventive"],
        "responsible": "Safety Officer",
        "target_date": (datetime.today() + timedelta(days=7)).strftime("%Y-%m-%d"),
        "status": "Open"
    }
