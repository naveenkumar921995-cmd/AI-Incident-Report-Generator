import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import cv2

# Add project root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import project modules
from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from src.risk_matrix import calculate_risk
from src.incident_classifier import classify_incident
from src.severity_predictor import predict_severity
from src.capa_generator import generate_capa
from src.trend_prediction import predict_trend
from src.hazard_detector import detect_hazard
from utils.document_exporter import export_to_word


# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="AI Incident Investigation Assistant",
    page_icon="🛠",
    layout="wide"
)

# ----------------------------------------------------
# ENTERPRISE STYLE CSS
# ----------------------------------------------------
def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.title("🛠 AI Incident Investigation Assistant")
st.caption("AI Powered Safety Investigation & Root Cause Analysis Platform")

st.divider()

# ----------------------------------------------------
# IMAGE HAZARD DETECTION
# ----------------------------------------------------
st.subheader("🧠 Hazard Detection from Image")

uploaded_file = st.file_uploader("Upload Incident Image", type=["jpg","png","jpeg"])

if uploaded_file:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    hazard = detect_hazard(image)

    st.warning(hazard)

st.divider()

# ----------------------------------------------------
# INCIDENT INPUT
# ----------------------------------------------------
st.subheader("Incident Description")

description = st.text_area(
    "Enter Incident Description",
    placeholder="Example: Worker slipped on oil spill near machine area"
)

# ----------------------------------------------------
# ANALYZE INCIDENT
# ----------------------------------------------------
if st.button("Analyze Incident"):

    if description.strip() == "":
        st.warning("Please enter an incident description.")
    else:

        with st.spinner("Analyzing incident using AI models..."):

            # Root Cause
            root_cause = predict_root_cause(description)

            st.subheader("Predicted Root Cause")
            st.success(root_cause)

            # Incident Classification
            incident_type = classify_incident(description)

            st.subheader("Incident Classification")
            st.info(incident_type)

            # Severity
            severity = predict_severity(root_cause)

            st.subheader("Incident Severity Level")
            st.metric("Severity Level", severity)

            # Risk Assessment
            likelihood, severity_val, risk_score, level = calculate_risk(root_cause)

            st.subheader("⚠ Risk Assessment")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Likelihood", likelihood)
            col2.metric("Severity", severity_val)
            col3.metric("Risk Score", risk_score)
            col4.metric("Risk Level", level)

            # ------------------------------------------------
            # RISK MATRIX
            # ------------------------------------------------
            st.subheader("Professional Risk Matrix")

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

            ax.scatter(likelihood-1, severity_val-1, s=200, marker="X")

            ax.set_xticks(range(5))
            ax.set_yticks(range(5))

            ax.set_xticklabels([1,2,3,4,5])
            ax.set_yticklabels([1,2,3,4,5])

            ax.set_xlabel("Likelihood")
            ax.set_ylabel("Severity")

            ax.set_title("5x5 Incident Risk Matrix")

            st.pyplot(fig)

            # ------------------------------------------------
            # RECOMMENDATIONS
            # ------------------------------------------------
            recommendations = recommend_actions(root_cause)

            st.subheader("Recommended Safety Actions")

            for r in recommendations:
                st.write("•", r)

            # ------------------------------------------------
            # CAPA
            # ------------------------------------------------
            capa = generate_capa(root_cause)

            st.subheader("Corrective Action")
            st.write(capa["corrective"])

            st.subheader("Preventive Action")
            st.write(capa["preventive"])

            # ------------------------------------------------
            # REPORT GENERATION
            # ------------------------------------------------
            report = generate_report(description, root_cause)

            st.subheader("Generated Investigation Report")

            st.code(report)

            # ------------------------------------------------
            # EXPORT REPORT
            # ------------------------------------------------
            if st.button("Export Report to Word"):

                file = export_to_word(report)

                st.success(f"Report Generated Successfully: {file}")

# ----------------------------------------------------
# ANALYTICS DASHBOARD
# ----------------------------------------------------
st.divider()

st.subheader("📊 Incident Analytics Dashboard")

try:

    data = pd.read_csv("data/incidents_dataset.csv")

    # Root Cause Chart
    fig = px.bar(
        data,
        x="root_cause",
        title="Incident Root Cause Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------------------
    # TREND PREDICTION
    # ------------------------------------------------
    st.subheader("📈 Incident Trend Prediction")

    if "incident_count" in data.columns:

        trend = predict_trend(data)

        trend_df = pd.DataFrame({
            "Future Period": range(1,7),
            "Predicted Incidents": trend
        })

        fig2 = px.line(
            trend_df,
            x="Future Period",
            y="Predicted Incidents",
            markers=True,
            title="Predicted Incident Trend"
        )

        st.plotly_chart(fig2, use_container_width=True)

except:
    st.info("Dataset not found for analytics.")
