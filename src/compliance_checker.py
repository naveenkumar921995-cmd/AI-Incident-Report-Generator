def detect_violation(root_cause):

    violations = {
        "Poor Housekeeping": "OSHA-1910.22 – Walking Working Surfaces",
        "Improper Tool Usage": "OSHA-1910.242 – Hand Tools",
        "Inadequate Lighting": "OSHA-1926.56 – Illumination"
    }

    return violations.get(root_cause, "General Safety Compliance Review Required")
