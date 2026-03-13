import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import project modules
from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from src.risk_matrix import calculate_risk
from src.safety_kpi import calculate_kpis
from src.safety_standards import get_safety_standard
from src.capa_engine import generate_capa
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
# SIDEBAR NAVIGATION
# -----------------------------
st.sidebar.title("AI Safety System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Incident Analysis",
        "Safety KPI Dashboard",
        "Incident Analytics",
        "About Project"
    ]
)


# =====================================================
# PAGE 1 : INCIDENT ANALYSIS
# =====================================================
if page == "Incident Analysis":

    st.title("🛠 AI Incident Investigation Assistant")
    st.caption("Machine Learning Powered Safety Investigation System")

    st.divider()

    description = st.text_area(
        "Enter Incident Description",
        placeholder="Example: Worker slipped on oil spill near machine area",
        height=120
    )

    if st.button("Analyze Incident"):

        if description.strip() == "":
            st.warning("Please enter incident description")

        else:

            with st.spinner("AI analyzing incident..."):

                # Root cause prediction
                root_cause = predict_root_cause(description)

                st.subheader("Predicted Root Cause")
                st.success(root_cause)

                # Safety standard
                standard = get_safety_standard(root_cause)

                st.subheader("Safety Standard Violation")

                st.write("Violation Code:", standard["violation_code"])
                st.write("Safety Standard:", standard["standard"])

                # CAPA actions
                capa = generate_capa(root_cause)

                st.subheader("Corrective Action")

                st.info(capa["corrective"])

                st.subheader("Preventive Action")

                st.info(capa["preventive"])

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

                fig, ax = plt.subplots(figsize=(4,3))

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

                st.subheader("Recommended Safety Actions")

                for r in recommendations:
                    st.write("•", r)

                # -----------------------------
                # REPORT GENERATION
                # -----------------------------
                report = generate_report(description, root_cause)

                st.subheader("Generated Investigation Report")

                st.text_area(
                    "Report",
                    report,
                    height=250
                )

                if st.button("Export Report to Word"):

                    file = export_to_word(report)

                    st.success(f"Report generated: {file}")


# =====================================================
# PAGE 2 : SAFETY KPI DASHBOARD
# =====================================================
elif page == "Safety KPI Dashboard":

    st.title("📊 Safety Monitoring Dashboard")

    try:

        data = pd.read_csv("data/incidents_dataset.csv")

        kpis = calculate_kpis(data)

        st.subheader("Safety Performance Indicators")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Incidents", kpis["Total Incidents"])
        col2.metric("Near Miss Reports", kpis["Near Miss Reports"])
        col3.metric("Unsafe Conditions", kpis["Unsafe Condition Reports"])

        col4, col5, col6 = st.columns(3)

        col4.metric("Closure Rate (%)", kpis["Closure Rate (%)"])
        col5.metric("Training Compliance (%)", kpis["Training Compliance (%)"])
        col6.metric("PPE Compliance (%)", kpis["PPE Compliance (%)"])

    except:
        st.warning("Dataset not found")


# =====================================================
# PAGE 3 : INCIDENT ANALYTICS
# =====================================================
elif page == "Incident Analytics":

    st.title("📈 Incident Analytics")

    try:

        data = pd.read_csv("data/incidents_dataset.csv")

        st.subheader("Root Cause Distribution")

        st.bar_chart(
            data["root_cause"].value_counts()
        )

        st.subheader("Incident Dataset")

        st.dataframe(data.head())

    except:
        st.warning("Dataset not found")


# =====================================================
# PAGE 4 : ABOUT PROJECT
# =====================================================
elif page == "About Project":

    st.title("About This Project")

    st.write("""
This system is an **AI-powered Incident Investigation Assistant**
designed to support workplace safety professionals.

### Key Features

• AI Root Cause Prediction  
• Risk Matrix Assessment  
• Safety Standard Violation Detection  
• CAPA (Corrective & Preventive Action) Engine  
• Safety Monitoring KPI Dashboard  
• Incident Analytics  

### Technology Stack

Python  
Machine Learning  
Streamlit  
Pandas  
Matplotlib  

This project demonstrates how **AI can support safety investigations
and risk management in industrial environments.**
""")
