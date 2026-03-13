def get_safety_standard(root_cause):

    standards = {

        "Poor housekeeping": {
            "violation_code": "DLF-HSE-01",
            "standard": "DLF Safety Manual Section 4.2",
            "bsc_reference": "BSC Workplace Transport & Housekeeping Standard",
            "description": "Workplace must be maintained clean and free from slip or trip hazards."
        },

        "Improper tool usage": {
            "violation_code": "DLF-HSE-07",
            "standard": "DLF Safety Manual Section 6.3",
            "bsc_reference": "BSC Safe Use of Work Equipment",
            "description": "All workers must use tools according to manufacturer and safety guidelines."
        },

        "Inadequate workplace lighting": {
            "violation_code": "DLF-HSE-12",
            "standard": "DLF Safety Manual Section 3.4",
            "bsc_reference": "BSC Workplace Environment Standards",
            "description": "Adequate illumination must be provided in all working areas."
        },

        "Unsafe work practice": {
            "violation_code": "DLF-HSE-15",
            "standard": "DLF Safety Manual Section 5.1",
            "bsc_reference": "BSC Behavioural Safety Standard",
            "description": "Workers must follow approved safe work procedures."
        }

    }

    return standards.get(root_cause, None)
