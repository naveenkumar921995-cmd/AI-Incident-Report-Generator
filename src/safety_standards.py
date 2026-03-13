def get_safety_standard(root_cause):

    standards = {
        "Human Error": {
            "violation_code": "BSC-HS-3.2",
            "standard": "British Safety Council - Worker Competency"
        },
        "Equipment Failure": {
            "violation_code": "DLF-SAFE-12",
            "standard": "DLF Equipment Safety Guideline"
        },
        "Unsafe Condition": {
            "violation_code": "OSHA-1910.22",
            "standard": "Walking Working Surfaces"
        }
    }

    return standards.get(root_cause, {
        "violation_code": "GEN-001",
        "standard": "General Safety Compliance"
    })
