def generate_report(description, root_cause):

    report = f"""
Incident Investigation Report

Incident Description:
{description}

Root Cause:
{root_cause}

Immediate Cause:
Unsafe condition detected during task.

Corrective Actions:
• Improve workplace inspection
• Conduct safety training
• Implement preventive controls

Conclusion:
This incident occurred due to {root_cause}.
Preventive actions should be implemented to avoid recurrence.
"""

    return report
