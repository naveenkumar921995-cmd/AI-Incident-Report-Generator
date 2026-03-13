from src.safety_standards import get_safety_standard
from src.capa_engine import generate_capa

def generate_report(description, root_cause):

    standard = get_safety_standard(root_cause)

    capa = generate_capa(root_cause)

    report = f"""
AI INCIDENT INVESTIGATION REPORT
--------------------------------

Incident Description
{description}

Root Cause
{root_cause}

Safety Standard Violation
Code: {standard['violation_code']}
Standard: {standard['standard']}

Corrective Action
{capa['corrective']}

Preventive Action
{capa['preventive']}

Monitoring Indexes
• Incident Frequency Rate
• Near Miss Reporting Rate
• Corrective Action Closure Rate
• PPE Compliance Monitoring

Appendix E – CAPA Guidance
Hierarchy of Controls Applied
1. Elimination
2. Engineering Control
3. Administrative Control
4. PPE
"""

    return report
