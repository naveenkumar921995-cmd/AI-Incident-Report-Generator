import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Incident Report Generator", layout="centered")

st.title("🤖 AI Incident Report Generator")
st.write("Generate professional facility incident reports using Generative AI.")

# User Inputs
location = st.text_input("Incident Location")
incident_time = st.time_input("Incident Time")
description = st.text_area("Incident Description")
action_taken = st.text_area("Action Taken")
status = st.selectbox("Current Status", ["Resolved", "Pending", "In Progress"])

if st.button("Generate Report"):

    prompt = f"""
    Create a professional facility incident report.

    Location: {location}
    Time: {incident_time}
    Description: {description}
    Action Taken: {action_taken}
    Status: {status}

    Format the report with:
    - Incident Summary
    - Action Taken
    - Final Status
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional facility management report writer."},
            {"role": "user", "content": prompt}
        ]
    )

    report = response.choices[0].message.content

    st.subheader("Generated Incident Report")

    st.write(report)

    st.download_button(
        label="Download Report",
        data=report,
        file_name=f"incident_report_{datetime.now().date()}.txt",
        mime="text/plain"
    )
