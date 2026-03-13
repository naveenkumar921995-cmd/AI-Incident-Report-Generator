# 🛠 AI Incident Investigation Assistant

An **AI-powered Incident Investigation and Safety Analytics Platform** designed to help organizations analyze workplace incidents, identify root causes, assess risk levels, and automatically generate professional investigation reports.

This project combines **Machine Learning, Safety Engineering principles, and AI-based analytics** to simulate a real-world **incident investigation management system** used in industries such as:

* Construction
* Manufacturing
* Infrastructure
* Oil & Gas
* Industrial Operations

---

# ⭐ Project Highlights

* 🤖 AI-powered **root cause prediction**
* 📊 **5×5 professional risk matrix analysis**
* 📋 **Corrective & Preventive Action (CAPA) system**
* 📑 **Automated incident investigation report generation**
* 📊 **Safety analytics dashboard**
* 🛡 **Safety compliance detection**
* 📅 **Incident investigation timeline management**
* 🖼 **Incident image upload support**
* 🌐 Interactive **Streamlit web application**

---

# 🚀 Live Application

🔗 **Live App**

https://ai-incident-report-generator-dszznbiuees8guy7gurwjj.streamlit.app/

The web application allows users to:

* Enter incident descriptions
* Predict root causes using AI
* Perform risk assessment
* Generate CAPA recommendations
* Track investigation details
* Export professional investigation reports

---

# 📌 Key Features

---

# 🔍 AI Root Cause Prediction

The system uses **Machine Learning with NLP techniques** to analyze incident descriptions and predict the most likely root cause.

Example:

```
Input:
Worker slipped on oil spill near machine area.

Output:
Root Cause → Poor Housekeeping
```

This helps safety teams **identify systemic issues quickly**.

---

# ⚠ Incident Classification

The application automatically categorizes incidents into standard workplace incident types:

* Near Miss
* First Aid Case
* Medical Treatment Case
* Lost Time Injury (LTI)
* Property Damage
* Environmental Incident

This ensures **structured and standardized incident reporting**.

---

# 📊 Risk Assessment & 5×5 Risk Matrix

The platform evaluates incident severity using a **professional industrial risk matrix** based on:

* Likelihood
* Severity
* Risk Score
* Risk Level

Benefits:

* Visual hazard prioritization
* Faster safety decision-making
* Identification of high-risk incidents

---

# 📈 Professional Risk Matrix Visualization

A visual **5×5 Risk Matrix** helps safety teams instantly understand the risk level of hazards.

Risk levels include:

* Low Risk
* Medium Risk
* High Risk
* Critical Risk

This enables organizations to **prioritize safety controls effectively**.

---

# 📋 Corrective & Preventive Actions (CAPA)

The system automatically recommends:

* **Corrective Actions** (Immediate fixes)
* **Preventive Actions** (Long-term safety improvements)

Example:

| Root Cause          | Corrective Action           | Preventive Action                           |
| ------------------- | --------------------------- | ------------------------------------------- |
| Poor housekeeping   | Clean oil spill immediately | Implement housekeeping inspection checklist |
| Improper tool usage | Stop unsafe work            | Conduct worker tool safety training         |
| Inadequate lighting | Install temporary lighting  | Implement monthly lighting inspection       |

CAPA fields include:

* Responsible person
* Target completion date
* Action status

This allows better **tracking of safety improvements**.

---

# 📅 Investigation Timeline Management

The system includes a structured **incident investigation timeline**.

Typical workflow:

| Investigation Step    | Timeline        |
| --------------------- | --------------- |
| Incident reported     | Immediate       |
| Investigation started | Within 24 hours |
| Root cause analysis   | Within 48 hours |
| CAPA implementation   | Within 7 days   |
| Investigation closure | Within 30 days  |

This ensures **timely and consistent incident investigations**.

---

# 🛡 Safety Standard Compliance Detection

The system detects potential **safety regulation violations** based on root causes.

Example:

| Root Cause          | Compliance Reference             |
| ------------------- | -------------------------------- |
| Poor Housekeeping   | Walking Working Surfaces Safety  |
| Improper Tool Usage | Hand Tool Safety                 |
| Inadequate Lighting | Workplace Illumination Standards |

This helps organizations **prepare for safety audits and regulatory compliance**.

---

# 📊 Incident Analytics Dashboard

The built-in analytics dashboard provides key insights such as:

* Total incidents
* Near miss reports
* High risk incidents
* Root cause distribution
* Incident trends

These analytics help organizations **identify recurring safety problems** and improve prevention strategies.

---

# 🧾 Automated Investigation Report Generation

The system automatically generates a **structured incident investigation report** including:

1. Incident description
2. Incident classification
3. Root cause analysis
4. Risk assessment
5. Safety standard violations
6. Corrective actions
7. Preventive actions
8. Investigation timeline
9. Monitoring and follow-up

Reports can be exported as **Word documents for official safety documentation**.

---

# 🖼 Incident Image Upload

Users can upload incident images to document the incident scene.

Current capabilities:

* Image documentation
* Visual reference for investigation

Future capability:

* AI-based **hazard detection using computer vision**

---

# 📷 Application Preview

You can add screenshots here for better GitHub presentation.

Example:

```
/screenshots

dashboard.png
risk_matrix.png
incident_report.png
```

Recommended screenshots:

* Incident analysis dashboard
* Risk matrix visualization
* Generated investigation report
* CAPA recommendation panel

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
│   ├── incident_classifier.py
│   ├── severity_predictor.py
│   ├── risk_matrix.py
│   ├── recommendation_engine.py
│   ├── capa_generator.py
│   ├── report_generator.py
│   ├── compliance_checker.py
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

```
Incident Description
        ↓
Text Preprocessing
        ↓
CountVectorizer (NLP)
        ↓
Feature Extraction
        ↓
Random Forest Classifier
        ↓
Root Cause Prediction
```

---

# 🛠 Technology Stack

| Category             | Technology       |
| -------------------- | ---------------- |
| Frontend             | Streamlit        |
| Programming Language | Python           |
| Data Processing      | Pandas, NumPy    |
| Machine Learning     | Scikit-Learn     |
| NLP                  | CountVectorizer  |
| Visualization        | Matplotlib       |
| Computer Vision      | OpenCV (planned) |
| Report Export        | python-docx      |

---

# ⚙ Installation Guide

## 1️⃣ Clone the Repository

```
git clone https://github.com/naveenkumar921995-cmd/AI-Incident-Report-Generator.git
```

---

## 2️⃣ Navigate to Project Folder

```
cd AI-Incident-Report-Generator
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

```
streamlit run app/streamlit_app.py
```

The application will open in your browser.

---

# 📊 Example Workflow

1️⃣ User enters incident description
2️⃣ AI predicts root cause
3️⃣ System classifies incident type
4️⃣ Risk matrix calculates severity
5️⃣ CAPA recommendations generated
6️⃣ Investigation report created
7️⃣ Report exported as Word document

---

# 🎯 Real-World Applications

This system can support:

* Construction safety management
* Industrial accident investigations
* Manufacturing safety analysis
* Workplace safety audits
* Environmental incident reporting
* Risk assessment automation

---

# 🚀 Future Improvements

Planned enhancements include:

* AI-powered investigation assistant
* Deep learning hazard detection
* Predictive incident trend forecasting
* Executive safety analytics dashboard
* Real-time safety monitoring
* Advanced compliance detection

---

# 👨‍💻 Author

**Naveen Kumar**

AI / Data Science Enthusiast
Machine Learning Projects | Safety Analytics | AI Applications

GitHub
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
