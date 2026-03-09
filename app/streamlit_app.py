import streamlit as st

from src.root_cause_predictor import predict_root_cause
from src.report_generator import generate_report
from src.recommendation_engine import recommend_actions
from utils.document_exporter import export_to_word

st.title("AI Incident Investigation Assistant")

description = st.text_area("Enter Incident Description")

if st.button("Analyze Incident"):

    root_cause = predict_root_cause(description)

    st.subheader("Predicted Root Cause")
    st.write(root_cause)

    recommendations = recommend_actions(root_cause)

    st.subheader("Recommended Actions")

    for r in recommendations:
        st.write("-", r)

    report = generate_report(description, root_cause)

    st.subheader("Generated Report")
    st.text(report)

    if st.button("Export Report"):

        file = export_to_word(report)
        st.success("Report Generated: " + file)
