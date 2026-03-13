import streamlit as st
import sys
import os
import pandas as pd

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from utils.document_exporter import export_to_word


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Incident Investigation Assistant",
    page_icon="🛠",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🛠 AI Incident Investigation Assistant")
st.caption("Machine Learning Powered Root Cause Analysis System")

st.divider()

# -----------------------------
# INCIDENT INPUT
# -----------------------------
st.subheader("Incident Description")

description = st.text_area(
    "Enter Incident Description",
    placeholder="Example: Worker slipped on oil spill near machine area"
)

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze Incident"):

    if description.strip() == "":
        st.warning("Please enter an incident description.")
    else:

        with st.spinner("Analyzing incident with AI..."):

            root_cause = predict_root_cause(description)

            st.subheader("Predicted Root Cause")
            st.success(root_cause)

            # Recommendations
            recommendations = recommend_actions(root_cause)

            st.subheader("Recommended Actions")

            for r in recommendations:
                st.write("•", r)

            # Generate report
            report = generate_report(description, root_cause)

            st.subheader("Generated Report")

            st.code(report)

            # Export button
            if st.button("Export Report to Word"):

                file = export_to_word(report)

                st.success(f"Report Generated: {file}")

# -----------------------------
# ANALYTICS DASHBOARD
# -----------------------------
st.divider()

st.subheader("📊 Incident Root Cause Analytics")

try:
    data = pd.read_csv("data/incidents_dataset.csv")

    st.bar_chart(data["root_cause"].value_counts())

except:
    st.info("Dataset not found for analytics.")
