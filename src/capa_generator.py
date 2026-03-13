def generate_capa(root_cause):

    capa = {

        "Poor housekeeping": {
            "corrective": "Clean affected work area immediately",
            "preventive": "Implement daily housekeeping inspection checklist"
        },

        "Improper tool usage": {
            "corrective": "Stop work and replace incorrect tools",
            "preventive": "Conduct tool usage training program"
        },

        "Inadequate workplace lighting": {
            "corrective": "Install temporary lighting",
            "preventive": "Conduct monthly lighting inspection"
        }

    }

    return capa.get(root_cause, {
        "corrective": "Conduct investigation",
        "preventive": "Implement safety awareness training"
    })
