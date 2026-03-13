def generate_capa(root_cause):

    capa = {
        "Human Error": {
            "corrective": "Provide immediate safety training",
            "preventive": "Introduce supervision and safety audits"
        },
        "Equipment Failure": {
            "corrective": "Repair faulty equipment",
            "preventive": "Implement preventive maintenance schedule"
        },
        "Unsafe Condition": {
            "corrective": "Remove hazard immediately",
            "preventive": "Introduce weekly safety inspection"
        }
    }

    return capa.get(root_cause, {
        "corrective": "Investigate and resolve issue",
        "preventive": "Improve safety procedures"
    })
