def recommend_actions(root_cause):

    recommendations = {
        "Poor housekeeping": [
            "Implement housekeeping inspections",
            "Provide spill cleanup kits",
            "Train workers on workplace cleanliness"
        ],

        "Improper tool usage": [
            "Provide proper tool training",
            "Conduct toolbox talks",
            "Inspect tools before work"
        ],

        "Inadequate workplace lighting": [
            "Install additional lighting",
            "Conduct lighting inspections"
        ]
    }

    return recommendations.get(root_cause, ["Conduct safety review"])
