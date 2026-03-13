from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_report(description, root_cause):

    prompt = f"""
    Generate a professional industrial safety investigation report.

    Incident:
    {description}

    Root Cause:
    {root_cause}

    Include:
    - Incident summary
    - Root cause analysis
    - Violation of safety standards
    - Corrective actions
    - Preventive actions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
