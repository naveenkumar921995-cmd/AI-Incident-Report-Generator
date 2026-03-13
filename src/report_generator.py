from src.safety_standards import get_safety_standard

def generate_report(description, root_cause):

    standard = get_safety_standard(root_cause)

    violation_code = standard["violation_code"]
    violation_desc = standard["description"]

    report = f"""
Incident Investigation Report
--------------------------------

Incident Description:
{description}

Root Cause:
{root_cause}

Safety Standard Violation:
{violation_code}

Violation Description:
{violation_desc}

Immediate Cause:
Unsafe condition detected during task.

Corrective Actions:
• Improve workplace inspection
• Conduct safety training
• Implement preventive controls

Conclusion:
Incident occurred due to {root_cause}.
This violates safety standard {violation_code}.
Preventive actions must be implemented.
"""

    return report
