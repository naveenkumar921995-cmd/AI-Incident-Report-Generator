from src.safety_standards import get_safety_standard


def generate_report(description, root_cause):

    standard = get_safety_standard(root_cause)

    if standard:

        violation_code = standard["violation_code"]
        dlf_standard = standard["standard"]
        bsc_standard = standard["bsc_reference"]
        description_std = standard["description"]

    else:
        violation_code = "N/A"
        dlf_standard = "N/A"
        bsc_standard = "N/A"
        description_std = "Standard not identified"

    report = f"""
================ INCIDENT INVESTIGATION REPORT ================

1. Incident Description
------------------------------------------------
{description}

2. Root Cause Identified by AI
------------------------------------------------
{root_cause}

3. Safety Standard Violation
------------------------------------------------
Violation Code: {violation_code}

DLF Safety Standard Reference:
{dlf_standard}

British Safety Council Standard:
{bsc_standard}

Standard Requirement:
{description_std}

4. Immediate Cause
------------------------------------------------
Unsafe condition detected during task execution.

5. Recommended Corrective Actions
------------------------------------------------
• Conduct workplace inspection
• Remove hazard and restore safe conditions
• Provide safety awareness training
• Implement preventive monitoring

6. Compliance Note
------------------------------------------------
The above violation must be corrected immediately
in accordance with DLF HSE compliance procedures
and British Safety Council best practices.

7. Conclusion
------------------------------------------------
This incident occurred due to {root_cause}.
Failure to comply with {violation_code} contributed
to the unsafe condition.

=================================================
"""

    return report
