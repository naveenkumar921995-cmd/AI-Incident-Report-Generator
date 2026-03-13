from src.severity_predictor import predict_severity
from src.capa_generator import generate_capa
from src.incident_classifier import classify_incident

def generate_report(description, root_cause):

    incident_type = classify_incident(description)

    severity = predict_severity(root_cause)

    capa = generate_capa(root_cause)

    report = f"""
AI INCIDENT INVESTIGATION REPORT

Incident Description
{description}

Incident Classification
{incident_type}

Root Cause
{root_cause}

Severity Level
{severity}

Corrective Action
{capa["corrective"]}

Preventive Action
{capa["preventive"]}

Conclusion
Investigation indicates incident occurred due to {root_cause}.
Preventive measures should be implemented immediately.
"""

    return report
