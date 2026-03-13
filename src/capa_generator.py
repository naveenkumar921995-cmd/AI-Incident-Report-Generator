def generate_capa(root_cause):

    capa = {

        "Poor housekeeping":[
            "Immediate spill cleanup",
            "Implement daily housekeeping inspection",
            "Assign area cleanliness responsibility"
        ],

        "Improper tool usage":[
            "Conduct tool safety training",
            "Inspect tools before shift",
            "Enforce PPE compliance"
        ],

        "Inadequate workplace lighting":[
            "Install additional lighting",
            "Conduct periodic lighting audits"
        ]

    }

    return capa.get(root_cause, ["Conduct safety investigation"])
