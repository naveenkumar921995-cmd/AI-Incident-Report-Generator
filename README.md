# AI Incident Report Generator

## Problem
Manually writing incident reports is slow and inconsistent.

## Solution
An AI-powered system that automatically:
- Analyzes incident descriptions
- Predicts root cause
- Generates structured reports
- Recommends preventive actions

## Tech Stack
Python
Streamlit
Scikit-learn
NLP

## Features
- Root Cause Prediction
- AI Generated Incident Reports
- Preventive Recommendations
- Export Report to PDF / DOCX

## Architecture
Streamlit UI
↓
NLP Processing
↓
ML Root Cause Prediction
↓
Recommendation Engine
↓
Report Generator
↓
Document Export

## Run Locally

```bash
git clone https://github.com/naveenkumar921995-cmd/AI-Incident-Report-Generator.git
cd AI-Incident-Report-Generator
pip install -r requirements.txt
streamlit run app/streamlit_app.py
