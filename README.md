# CertPrep - Professional Certification Prep App

CertPrep is a fast, elegant, and modular web application designed to help cloud professionals prepare for certification exams (supporting **Google Cloud**, **AWS**, **dbt**, and **Microsoft**). 

The app features a premium glassmorphic layout with persistent sidebar menus, interactive quiz flows, a timed exam simulation mode, custom difficulty tiers, study cheat sheets, and in-depth scorecard reviews.

---

## 🎨 Key Features

- **Persistent Sidebar Navigation**: Quickly navigate between top-level providers (**Google Cloud**, **AWS**, **dbt**, and **Microsoft**) using a modern left-side panel (responsive drawer on mobile) featuring SVGs of their actual logos.
- **Difficulty Tier Selector**: Customise your study session by choosing between **Easy** (foundational concepts), **Medium** (practical scenarios), or **Hard** (architectural troubleshooting) questions.
- **Four Study Modes & Dashboard Tabs**:
  - **📝 Practice Exams**: Customise your study session by choosing between **Easy**, **Medium**, or **Hard** levels. Select between untimed *Practice Mode* (instant answers and explanations) or timed *Exam Simulation* (20-question, 20-minute simulated tests with dynamic navigation and review flags).
  - **📑 Study Cheat Sheets**: Outline core concepts, common CLI command structures, and architectural patterns.
  - **🎴 Study Flashcards**: Active-recall Q&A flashcards covering service definitions, limits, commands, and common gotchas.
  - **📋 Exam Guide Checklist**: Flip-based domain-by-domain breakdowns of the official exam guide with a skills checklist.
- **Interactive Question Navigation Grid**: A visual map displaying answered, current, and flagged questions, allowing users to jump directly to any question during simulations.
- **Detailed Scorecard Review**: After completion, view your percentage score, a color-coded success badge, and an expandable accordion breakdown of every question to inspect your choices, correct options, and detailed explanations.
- **High-Quality Question Pool**: Includes at least **50 realistic questions** per certification (**14 certifications, 700 questions total** in the compiled database), tagged by difficulty.
- **Theme Customization**: Beautiful glassmorphism theme, with a theme switcher supporting persistent dark-mode and light-mode preferences.

---

## 🛠️ Technology Stack

- **Backend**: Python 3 & Flask
- **Frontend**: Vanilla HTML5, Vanilla CSS3 (Custom properties/variables, responsive layouts, animations), and Vanilla JavaScript (Fetch API, zero frameworks)
- **Data Store**: Structured JSON database (`data/questions.json`)
- **Utility Script**: Programmatic database compiler (`scripts/populate_questions.py`)

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

5. **Generate the Question Bank**:
   Generate the 700-question database by running the python compiler script:
   ```bash
   python3 scripts/populate_questions.py
   ```

6. **Run the Flask Server**:
   ```bash
   python app.py
   ```

7. **Open Your Browser**:
   Navigate to **[http://localhost:8080](http://localhost:8080)** to start practicing!

---

## 📁 File Structure

```text
certification-prep-app/
├── app.py                 # Flask server & backend API endpoints
├── data/
│   └── questions.json     # 700-question database mapped by provider & difficulty
├── scripts/
│   └── populate_questions.py # Programmatic question bank generator script
├── static/
│   ├── css/
│   │   └── style.css      # Custom properties, sidebars, timers, and accordions
│   └── js/
│       └── app.js         # Single-Page-App state manager, timers, & navigators
├── templates/
│   └── index.html         # Sidebar, exam configurations, & question reviews markup
├── .gitignore             # Git exclusion rules
└── README.md              # Project documentation
```

---

## 🔧 Expanding with More Certifications

To add a new exam provider or certificate:
1. Append your exam configuration, topic matrices, and questions (divided into `easy`, `medium`, and `hard` profiles) to `scripts/populate_questions.py`.
2. Re-run `python3 scripts/populate_questions.py` to compile the updated JSON.
3. Update the `providers` dictionary in `static/js/app.js` to define the provider name, icon, and description if adding a new provider.

The client-side dashboard will dynamically load the new categories, count the exams, and render selection buttons automatically.
