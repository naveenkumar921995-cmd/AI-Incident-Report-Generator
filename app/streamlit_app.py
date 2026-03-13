import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import project modules
from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from src.risk_matrix import calculate_risk
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

            # Predict root cause
            root_cause = predict_root_cause(description)

            st.subheader("Predicted Root Cause")
            st.success(root_cause)

            # -----------------------------
            # -----------------------------
# RISK ASSESSMENT
# -----------------------------
likelihood, severity, risk_score, level = calculate_risk(root_cause)

st.subheader("⚠ Risk Assessment")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Likelihood", likelihood)
col2.metric("Severity", severity)
col3.metric("Risk Score", risk_score)
col4.metric("Risk Level", level)
            # RISK MATRIX CHART
            # -----------------------------
            st.subheader("Risk Matrix")

            fig, ax = plt.subplots()

            ax.scatter(likelihood, severity, s=250)

            ax.set_xlabel("Likelihood")
            ax.set_ylabel("Severity")

            ax.set_xlim(0, 5)
            ax.set_ylim(0, 5)

            ax.set_title("Incident Risk Matrix")

            st.pyplot(fig)

            # -----------------------------
            # RECOMMENDATIONS
            # -----------------------------
            recommendations = recommend_actions(root_cause)

            st.subheader("Recommended Actions")

            for r in recommendations:
                st.write("•", r)

            # -----------------------------
            # REPORT GENERATION
            # -----------------------------
            report = generate_report(description, root_cause)

            st.subheader("Generated Report")

            st.code(report)

            # -----------------------------
            # EXPORT REPORT
            # -----------------------------
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
