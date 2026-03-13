import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import modules
from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from src.risk_matrix import calculate_risk
from src.incident_classifier import classify_incident
from src.severity_predictor import predict_severity
from src.capa_generator import generate_capa
from src.compliance_checker import detect_violation
from utils.document_exporter import export_to_word


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="AI Incident Investigation Assistant",
    page_icon="🛠",
    layout="wide"
)

# ------------------------------------------------
# CUSTOM STYLE
# ------------------------------------------------

def load_css():
    css = """
    <style>
    .main {
        background-color:#f5f7fb;
    }

    .block-container {
        padding-top:2rem;
    }

    h1,h2,h3 {
        font-weight:600;
    }

    .metric-box{
        background:white;
        padding:20px;
        border-radius:10px;
        box-shadow:0px 1px 5px rgba(0,0,0,0.1);
    }
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

load_css()


# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.title("🛠 AI Incident Investigation Assistant")
st.caption("AI Powered Safety Investigation & Root Cause Analysis System")

st.divider()

# ------------------------------------------------
# INCIDENT DESCRIPTION
# ------------------------------------------------

st.subheader("Incident Description")

description = st.text_area(
    "Enter Incident Description",
    placeholder="Example: Worker slipped on oil spill near machine area"
)

# ------------------------------------------------
# IMAGE UPLOAD
# ------------------------------------------------

st.subheader("Upload Incident Image (Optional)")

uploaded_image = st.file_uploader(
    "Upload image",
    type=["jpg","png","jpeg"]
)

if uploaded_image:
    st.image(uploaded_image)
    st.info("AI Hazard Detection Module (Future Upgrade)")


# ------------------------------------------------
# ANALYZE INCIDENT
# ------------------------------------------------

if st.button("Analyze Incident"):

    if description.strip()=="":
        st.warning("Please enter incident description")

    else:

        with st.spinner("Analyzing incident using AI..."):

            # -----------------------------------
            # ROOT CAUSE
            # -----------------------------------

            root_cause = predict_root_cause(description)

            st.subheader("Predicted Root Cause")

            st.success(root_cause)


            # -----------------------------------
            # INCIDENT TYPE
            # -----------------------------------

            incident_type = classify_incident(description)

            st.subheader("Incident Classification")

            st.info(incident_type)


            # -----------------------------------
            # SEVERITY
            # -----------------------------------

            severity = predict_severity(root_cause)

            st.subheader("Incident Severity Level")

            st.metric("Severity", severity)


            # -----------------------------------
            # RISK MATRIX
            # -----------------------------------

            likelihood,severity_val,risk_score,level = calculate_risk(root_cause)

            st.subheader("Risk Assessment")

            col1,col2,col3,col4 = st.columns(4)

            col1.metric("Likelihood", likelihood)
            col2.metric("Severity", severity_val)
            col3.metric("Risk Score", risk_score)
            col4.metric("Risk Level", level)


            # -----------------------------------
            # RISK MATRIX VISUAL
            # -----------------------------------

            st.subheader("Professional Risk Matrix")

            matrix = [
                [1,2,3,4,5],
                [2,4,6,8,10],
                [3,6,9,12,15],
                [4,8,12,16,20],
                [5,10,15,20,25]
            ]

            fig, ax = plt.subplots(figsize=(5,4))

            ax.imshow(matrix)

            for i in range(5):
                for j in range(5):
                    ax.text(j,i,matrix[i][j], ha="center",va="center")

            ax.scatter(likelihood-1,severity_val-1,s=200,marker="X")

            ax.set_xticks(range(5))
            ax.set_yticks(range(5))

            ax.set_xlabel("Likelihood")
            ax.set_ylabel("Severity")

            st.pyplot(fig)


            # -----------------------------------
            # SAFETY VIOLATION
            # -----------------------------------

            violation = detect_violation(root_cause)

            st.subheader("Safety Standard Violation")

            st.warning(violation)


            # -----------------------------------
            # RECOMMENDATIONS
            # -----------------------------------

            st.subheader("Recommended Safety Actions")

            rec = recommend_actions(root_cause)

            for r in rec:
                st.write("•", r)


            # -----------------------------------
            # CAPA
            # -----------------------------------

            capa = generate_capa(root_cause)

            st.subheader("Corrective Action")

            st.write(capa["corrective"])

            st.subheader("Preventive Action")

            st.write(capa["preventive"])

            st.subheader("Responsible Person")

            st.write(capa["responsible"])

            st.subheader("Target Completion Date")

            st.write(capa["target_date"])

            st.subheader("Action Status")

            st.write(capa["status"])


            # -----------------------------------
            # INVESTIGATION TIMELINE
            # -----------------------------------

            st.subheader("Investigation Timeline")

            timeline = {
                "Incident Reported":"Immediate",
                "Investigation Start":"Within 24 hrs",
                "Root Cause Analysis":"Within 48 hrs",
                "CAPA Implementation":"Within 7 days",
                "Investigation Closure":"Within 30 days"
            }

            timeline_df = pd.DataFrame(
                timeline.items(),
                columns=["Step","Timeline"]
            )

            st.table(timeline_df)


            # -----------------------------------
            # REPORT GENERATION
            # -----------------------------------

            report = generate_report(
                description,
                root_cause,
                level,
                capa
            )

            st.subheader("Generated Investigation Report")

            st.code(report)


            # -----------------------------------
            # EXPORT REPORT
            # -----------------------------------

            if st.button("Export Report to Word"):

                file = export_to_word(report)

                st.success(f"Report Generated Successfully: {file}")


# ------------------------------------------------
# ANALYTICS DASHBOARD
# ------------------------------------------------

st.divider()

st.subheader("Incident Analytics Dashboard")

try:

    data = pd.read_csv("data/incidents_dataset.csv")

    # KPI
    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Incidents", len(data))
    col2.metric("Near Miss", len(data[data["incident_type"]=="Near Miss"]))
    col3.metric("High Risk", len(data[data["risk_level"]=="High"]))
    col4.metric("CAPA Open", len(data[data["status"]=="Open"]))

    st.subheader("Root Cause Distribution")

    st.bar_chart(data["root_cause"].value_counts())

except:

    st.info("Dataset not available for analytics")
