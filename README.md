# CertPrep - Modular Certification Preparation App

CertPrep is a fast, elegant, and modular web application designed to help cloud professionals prepare for certification exams (e.g., **Google Associate Cloud Engineer** and **AWS Certified Cloud Practitioner**). 

The app features a premium, modern design with a glassmorphic aesthetic, interactive quiz flows, instant feedback with explanations, and a scorecard summary at the end of each session.

---

## 🎨 Key Features

- **Multi-Exam Dashboard**: Choose from different certifications dynamically loaded from a single question bank.
- **Interactive Quiz View**: Practice mode showing one multiple-choice question at a time with clean, card-styled option selectors.
- **Immediate Feedback**: Instantly displays correct/incorrect answers with color highlights (green/red) and in-depth educational explanations.
- **Rich Scorecard Summary**: Computes a percentage score, presents a dynamic visual status badge, and evaluates readiness (passing benchmark set at 70%).
- **Theme Customization**: Beautiful default dark-mode styling with a toggle switch to a clean light-mode theme (with preference persistent in `localStorage`).
- **Zero Frontend Frameworks**: Built using only plain vanilla HTML5, CSS3, and ES6+ JavaScript with standard Fetch API requests.

---

## 🛠️ Technology Stack

- **Backend**: Python 3 & Flask
- **Frontend**: Vanilla HTML5, Vanilla CSS3 (Custom properties/variables, animations), and Vanilla JavaScript (Fetch API)
- **Data Store**: Structured JSON database (`data/questions.json`)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Setup Instructions

1. **Clone the Repository** (or navigate to the project directory):
   ```bash
   cd certification-prep-app
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install flask
   ```

5. **Run the Flask Server**:
   ```bash
   python app.py
   ```

6. **Open Your Browser**:
   Navigate to **[http://localhost:8080](http://localhost:8080)** to start practicing!

---

## 📁 File Structure

```text
certification-prep-app/
├── app.py                 # Flask server & backend API endpoints
├── data/
│   └── questions.json     # Modular database mapping certification categories & questions
├── static/
│   ├── css/
│   │   └── style.css      # Glassmorphic dark/light styles, animations, & variables
│   └── js/
│       └── app.js         # Single-Page-App client logic, Fetch API, & quiz flow
├── templates/
│   └── index.html         # Main dashboard, quiz layout, & scorecard structure
├── .gitignore             # Git exclusion rules
└── README.md              # Project documentation
```

---

## 🔧 Expanding with More Certifications

Adding a new certification (e.g., *Azure Fundamentals* or *Google Cloud Digital Leader*) is extremely simple. Just append a new certification object to the `"certifications"` array inside `data/questions.json`:

```json
{
  "id": "microsoft-azure-fundamentals",
  "name": "Microsoft Azure Fundamentals (AZ-900)",
  "description": "Validates foundational knowledge of cloud services and how those services are provided with Microsoft Azure.",
  "icon": "☁️",
  "questions": [
    {
      "id": "az-900-1",
      "question": "Which cloud service model provides maximum user control over the underlying operating systems and networking hardware?",
      "options": [
        "Software as a Service (SaaS)",
        "Platform as a Service (PaaS)",
        "Infrastructure as a Service (IaaS)",
        "Serverless Computing"
      ],
      "correctAnswerIndex": 2,
      "explanation": "Infrastructure as a Service (IaaS) provides virtualized computing resources over the internet, giving users full access and management control over operating systems, storage, and networking."
    }
  ]
}
```

The Flask API will automatically read this data and dynamically render it on the home dashboard!
