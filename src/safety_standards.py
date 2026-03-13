def get_safety_standard(root_cause):

    standards = {

        "Poor housekeeping": {
            "standard": "BSC-HS-3.2",
            "description": "Workplace must be maintained clean and free from spill hazards"
        },

        "Improper tool usage": {
            "standard": "OSHA-1926.300",
            "description": "Tools must be used according to manufacturer safety guidelines"
        },

        "Inadequate workplace lighting": {
            "standard": "BSC-HS-5.1",
            "description": "Work areas must have adequate lighting for safe operations"
        }

    }

    return standards.get(root_cause, {
        "standard": "GEN-SAFE-01",
        "description": "General workplace safety violation"
    })
