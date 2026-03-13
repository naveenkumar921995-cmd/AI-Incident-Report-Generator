# 🛠 AI Incident Investigation Assistant

An **AI-powered Safety Investigation Platform** that helps organizations analyze workplace incidents, identify root causes, evaluate risks, and generate professional investigation reports automatically.

This project combines **Machine Learning, Safety Engineering principles, and AI-driven analytics** to simulate a real-world **incident investigation management system** used in industries such as construction, manufacturing, oil & gas, and infrastructure projects.

---

# 🚀 Live Application

🔗 **Live App:**
https://ai-incident-report-generator-dszznbiuees8guy7gurwjj.streamlit.app/

---

# 📌 Key Features

### 🔍 AI Root Cause Prediction

Uses a **machine learning model (Random Forest + NLP)** to analyze incident descriptions and predict the most likely root cause.

Example:

```
Input:
Worker slipped on oil spill near machine area.

Output:
Root Cause → Poor Housekeeping
```

---

### ⚠ Incident Classification

Automatically categorizes incidents into types such as:

* Near Miss
* First Aid Case
* Medical Treatment Case
* Lost Time Injury (LTI)
* Property Damage
* Environmental Incident

---

### 📊 Risk Assessment & Risk Matrix

The system evaluates incident risk using a **5×5 risk matrix** based on:

* Likelihood
* Severity
* Risk Score
* Risk Level

Visual risk matrix helps safety professionals quickly identify **critical hazards**.

---

### 🧠 Hazard Detection from Images

Users can upload incident images to detect potential hazards.

Capabilities:

* Image-based hazard indication
* Visual inspection support
* Quick incident assessment

---

### 📋 Corrective & Preventive Actions (CAPA)

Automatically generates safety actions based on root cause:

Examples:

| Root Cause          | Corrective Action          | Preventive Action              |
| ------------------- | -------------------------- | ------------------------------ |
| Poor housekeeping   | Clean affected area        | Implement inspection checklist |
| Improper tool usage | Stop unsafe work           | Conduct tool usage training    |
| Inadequate lighting | Install temporary lighting | Monthly lighting inspection    |

---

### 📈 Incident Trend Prediction

Predicts **future incident patterns** using historical data.

Helps organizations:

* Identify recurring safety issues
* Predict incident growth
* Improve preventive planning

---

### 📊 Safety Analytics Dashboard

Interactive analytics dashboard provides:

* Root cause distribution
* Incident trend analysis
* Safety performance insights

Charts are built using **Plotly for professional dashboard visualization**.

---

### 📄 Automatic Investigation Report Generation

The system automatically generates a **structured incident investigation report** including:

* Incident description
* Root cause analysis
* Risk assessment
* Corrective actions
* Preventive actions
* Investigation summary

Reports can be exported as **Word documents for official documentation**.

---

# 🏗 Project Architecture

```
AI-Incident-Report-Generator
│
├── app
│   ├── streamlit_app.py
│   └── style.css
│
├── data
│   └── incidents_dataset.csv
│
├── src
│   ├── root_cause_predictor.py
│   ├── report_generator.py
│   ├── recommendation_engine.py
│   ├── incident_classifier.py
│   ├── severity_predictor.py
│   ├── capa_generator.py
│   ├── risk_matrix.py
│   ├── hazard_detector.py
│   └── trend_prediction.py
│
├── utils
│   └── document_exporter.py
│
├── requirements.txt
└── README.md
```

---

# 🧠 Machine Learning Pipeline

### Text Processing

```
Incident Description
        ↓
CountVectorizer (NLP)
        ↓
Feature Extraction
        ↓
RandomForestClassifier
        ↓
Root Cause Prediction
```

---

# 🛠 Technology Stack

| Category         | Technology         |
| ---------------- | ------------------ |
| Frontend         | Streamlit          |
| Data Processing  | Pandas, NumPy      |
| Machine Learning | Scikit-Learn       |
| Visualization    | Matplotlib, Plotly |
| Computer Vision  | OpenCV             |
| NLP              | CountVectorizer    |
| Report Export    | python-docx        |

---

# ⚙ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/naveenkumar921995-cmd/AI-Incident-Report-Generator.git
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Application

```
streamlit run app/streamlit_app.py
```

---

# 📊 Example Workflow

1️⃣ User enters incident description
2️⃣ AI predicts root cause
3️⃣ System classifies incident type
4️⃣ Risk matrix calculates severity
5️⃣ CAPA recommendations generated
6️⃣ Investigation report generated
7️⃣ Report exported for documentation

---

# 🎯 Real-World Applications

This system can be used for:

* Construction safety management
* Industrial accident investigation
* Manufacturing incident analysis
* Workplace safety audits
* Environmental incident reporting

---

# 🚀 Future Improvements

Planned upgrades:

* 🤖 LLM-powered investigation reports
* 🧠 AI hazard detection using deep learning
* 📊 Executive safety dashboard
* 📈 Predictive safety analytics
* 📷 Real-time safety camera monitoring
* 🧾 OSHA / Safety standard compliance tagging

---

# 👨‍💻 Author

**Naveen Kumar**

AI / Data Science Enthusiast
Machine Learning Projects | Safety Analytics | AI Applications

GitHub:
https://github.com/naveenkumar921995-cmd

---

# ⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

# 📜 License

This project is open-source and available under the **MIT License**.
