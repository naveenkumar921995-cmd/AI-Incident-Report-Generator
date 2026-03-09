def generate_report(description, root_cause):

    summary = f"""
AI Investigation Summary

The incident described as:
"{description}"

has been analyzed using a machine learning model.

The most probable root cause identified is:
{root_cause}.

This suggests that the incident likely occurred due to unsafe conditions or inadequate preventive controls related to {root_cause.lower()}.
"""

    report = f"""
INCIDENT INVESTIGATION REPORT

-------------------------------------

Incident Description:
{description}

Predicted Root Cause:
{root_cause}

Immediate Cause:
Unsafe condition detected during task.

Corrective Actions:
• Improve workplace inspections
• Conduct safety training programs
• Implement preventive control measures
• Monitor compliance with safety procedures

AI Investigation Summary:
{summary}

Conclusion:
This incident occurred due to {root_cause}.  
Appropriate corrective and preventive actions must be implemented to prevent recurrence.
"""

    return report
