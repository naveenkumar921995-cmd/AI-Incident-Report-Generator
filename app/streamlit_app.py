import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
# CUSTOM STYLE
# -----------------------------
st.markdown("""
<style>

.main-title {
    font-size:30px;
    font-weight:700;
}

.small-text {
    font-size:14px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
st.markdown('<p class="main-title">🛠 AI Incident Investigation Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="small-text">Machine Learning Powered Root Cause Analysis System</p>', unsafe_allow_html=True)

st.divider()


# -----------------------------
# INCIDENT INPUT
# -----------------------------
st.subheader("Incident Description")

description = st.text_area(
    "Enter Incident Description",
    placeholder="Example: Worker slipped on oil spill near machine area",
    height=120
)

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("Analyze Incident"):

    if description.strip() == "":
        st.warning("Please enter an incident description.")

    else:

        with st.spinner("Analyzing incident with AI..."):

            # -----------------------------
            # ROOT CAUSE PREDICTION
            # -----------------------------
            root_cause = predict_root_cause(description)

            st.subheader("Predicted Root Cause")
            st.success(root_cause)

            # -----------------------------
            # RISK ASSESSMENT
            # -----------------------------
            likelihood, severity, risk_score, level = calculate_risk(root_cause)

            st.subheader("Risk Assessment")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Likelihood", likelihood)
            col2.metric("Severity", severity)
            col3.metric("Risk Score", risk_score)
            col4.metric("Risk Level", level)

            # -----------------------------
            # RISK MATRIX
            # -----------------------------
            st.subheader("Risk Matrix")

            fig, ax = plt.subplots(figsize=(5,4))

            matrix = [
                [1,2,3,4,5],
                [2,4,6,8,10],
                [3,6,9,12,15],
                [4,8,12,16,20],
                [5,10,15,20,25]
            ]

            ax.imshow(matrix)

            for i in range(5):
                for j in range(5):
                    ax.text(j, i, matrix[i][j], ha="center", va="center")

            ax.scatter(likelihood-1, severity-1, s=120, marker="X")

            ax.set_xticks(range(5))
            ax.set_yticks(range(5))

            ax.set_xticklabels([1,2,3,4,5])
            ax.set_yticklabels([1,2,3,4,5])

            ax.set_xlabel("Likelihood")
            ax.set_ylabel("Severity")

            ax.set_title("5x5 Risk Matrix")

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

            st.text_area(
                "Investigation Report",
                report,
                height=250
            )

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

st.subheader("Incident Root Cause Analytics")

try:

    data = pd.read_csv("data/incidents_dataset.csv")

    st.bar_chart(
        data["root_cause"].value_counts(),
        height=300
    )

except:
    st.info("Dataset not found for analytics.")
