def classify_incident(description):

    description = description.lower()

    if "death" in description or "fatal" in description:
        return "Fatality"

    if "fracture" in description or "hospital" in description:
        return "Lost Time Injury"

    if "cut" in description or "minor injury" in description:
        return "First Aid Case"

    if "spill" in description or "leak" in description:
        return "Environmental Incident"

    if "damage" in description:
        return "Property Damage"

    return "Near Miss"
