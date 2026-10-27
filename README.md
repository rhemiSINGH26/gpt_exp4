# 🎓 Personalized Learning Recommendation System (gpt_exp4)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E.svg?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, interactive **Personalized Learning & Course Recommendation System** built with **Python**, **Flask**, and **Vanilla JavaScript**. It profiles student interests, skill levels, learning styles, and career goals to generate tailored, scored study tracks with human-readable rationale and real-time feedback refinement.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Domain & Curriculum Coverage](#-domain--curriculum-coverage)
- [Repository Structure](#-repository-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [REST API Reference](#-rest-api-reference)
- [Scoring & Recommendation Engine](#-scoring--recommendation-engine)
- [Interactive Feedback Loop](#-interactive-feedback-loop)
- [License](#-license)

---

## 🌟 Overview

Navigating online education and deciding what to learn next can be overwhelming. Learners often struggle with curriculum sequences that don't match their current skill level, preferred methodology (hands-on projects vs. theory), or specific career aspirations.

**Personalized Learning Recommendation System** solves this by:
1. **Capturing Comprehensive User Profiles**: Captures learner academic field, specific technologies of interest, current proficiency (Beginner, Intermediate, Advanced), and learning style preferences (Practical, Theoretical, Both).
2. **Scoring & Deduplication**: Matches aspirations against specialized curriculum tracks (AI, Java, Python, Cybersecurity, Web Development, and Core CS) and assigns matching scores (up to 95%).
3. **Explaining Recommendations**: Provides transparent, personalized justifications for each suggested course.
4. **Interactive Real-Time Refinement**: Incorporates a built-in feedback loop that adapts recommendations instantly based on learner comments.

---

## 🚀 Key Features

| Capability | Description |
| :--- | :--- |
| **👤 Detailed Learner Profiling** | Collects user name, age, field of study, specific technology interests, current experience level, and preferred pedagogy. |
| **🎯 Goal-Aware Course Matching** | Matches high-level career goals (e.g., *"Learn AI and build computer vision models"*) with targeted modules. |
| **📊 Scored Recommendations** | Ranks candidates by relevance percentage score (e.g., 95% Match) and limits results to top 5 deduplicated tracks. |
| **💡 Transparent Reasoning** | Every recommended course includes an explicit explanation of *why* it was chosen for the learner. |
| **🔄 Live Feedback Loop** | Allows users to provide natural language adjustments (e.g., *"I prefer backend Java over frontend"*), instantly updating results. |
| **🌐 Full RESTful JSON API** | Exposes `/recommend` endpoint for seamless integration into web apps, mobile apps, or LMS platforms. |
| **📱 Responsive Modern UI** | Clean, mobile-friendly interface designed with CSS Grid, cards, responsive layouts, and loading states. |

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User([Learner / Student]) --> Input[Fill Profile & Learning Goals]
    Input --> WebUI[Web Interface: templates/index.html]
    WebUI --> JS[static/script.js: fetch API]
    
    JS -->|POST /recommend (JSON)| Flask[Flask Backend: app.py]
    
    subgraph Engine ["Recommendation Engine: generate_recommendations()"]
        Flask --> Parse[Parse & Normalize: interests, skill_level, learning_type, goal]
        Parse --> RuleMatch{Domain Matchers}
        RuleMatch -->|Java| JavaTrack[Java Fundamentals, OOP, Data Structures, Spring Boot]
        RuleMatch -->|AI / ML| AITrack[AI Fundamentals, ML Basics, Generative AI, Deep Learning, Vision]
        RuleMatch -->|Python| PyTrack[Python Programming, Data Science, Machine Learning with Python]
        RuleMatch -->|Security| SecTrack[Cybersecurity Fundamentals, Network Security, Ethical Hacking]
        RuleMatch -->|Web Dev| WebTrack[HTML/CSS, JavaScript, Full Stack Development]
        RuleMatch -->|General / Fallback| DefTrack[Programming Fundamentals, Data Structures, Projects]
        
        JavaTrack --> Consolidate[Deduplicate Unique Courses]
        AITrack --> Consolidate
        PyTrack --> Consolidate
        SecTrack --> Consolidate
        WebTrack --> Consolidate
        DefTrack --> Consolidate
        
        Consolidate --> Sort[Sort by Match Score Descending]
        Sort --> Top5[Extract Top 5 Recommendations]
    end

    Top5 -->|JSON Response| JS
    JS --> Render[Dynamically Render Recommendation Cards with Match Scores]
    Render --> FeedbackSection[Display Interactive Feedback Section]

    FeedbackSection -->|Feedback Input| Update[updateRecommendations()]
    Update -->|Append Feedback & Re-fetch| JS
```

---

## 📚 Domain & Curriculum Coverage

The built-in catalog provides structured modules across high-demand disciplines:

### 1. Java Ecosystem
- **Java Programming Fundamentals** (Score: 95) — Core syntax, data types, control flow.
- **Object-Oriented Programming with Java** (Score: 92) — Inheritance, polymorphism, encapsulation, abstraction.
- **Java Data Structures** (Score: 88) — Collections, lists, trees, and algorithm design.
- **Java Mini Projects** (Score: 86) — Hands-on problem-solving and software development.
- **Spring Boot Development** (Score: 82) — Enterprise web applications, microservices, and REST APIs.

### 2. Artificial Intelligence & Machine Learning
- **Artificial Intelligence Fundamentals** (Score: 95) — Search algorithms, heuristics, expert systems.
- **Machine Learning Basics** (Score: 92) — Supervised, unsupervised learning, regression, classification.
- **Generative AI** (Score: 90) — Large Language Models, prompt engineering, generative architectures.
- **Deep Learning Fundamentals** (Score: 87) — Neural networks, backpropagation, PyTorch/TensorFlow.
- **Computer Vision** (Score: 84) — Image classification, object detection, convolutional networks.

### 3. Python & Data Science
- **Python Programming** (Score: 95) — Scripting, automation, standard libraries.
- **Python for Data Science** (Score: 91) — NumPy, Pandas, data exploration, visualization.
- **Machine Learning with Python** (Score: 89) — Scikit-learn pipelines, model training, evaluation.

### 4. Cybersecurity
- **Cybersecurity Fundamentals** (Score: 95) — Core threat landscapes, CIA triad, security hygiene.
- **Network Security** (Score: 92) — Firewalls, protocols, traffic analysis, defense-in-depth.
- **Ethical Hacking Fundamentals** (Score: 89) — Penetration testing, vulnerability discovery, scanning.

### 5. Web Development
- **HTML and CSS** (Score: 94) — Responsive layouts, modern CSS Grid/Flexbox.
- **JavaScript Programming** (Score: 91) — DOM manipulation, asynchronous programming, APIs.
- **Full Stack Development** (Score: 88) — Client-server integration, databases, deployment.

---

## 📂 Repository Structure

```
├── static/
│   ├── script.js                # Frontend asynchronous API communication & UI rendering
│   └── style.css                # Clean, responsive CSS stylesheet (cards, grid, buttons)
├── templates/
│   └── index.html               # Semantic HTML5 single-page application
├── app.py                       # Flask server and recommendation engine logic
├── requirements.txt             # Python dependencies (Flask)
├── .gitignore                   # Standard ignore rules
├── LICENSE                      # MIT Open Source License
└── README.md                    # Project documentation
```

---

## ⚙️ Prerequisites

- **Python 3.9+** installed on your system.

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rhemiSINGH26/gpt_exp4.git
cd gpt_exp4
```

### 2. Create and Activate a Virtual Environment
- **On Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🎮 Running the Application

### 1. Start the Flask Server
```bash
python app.py
```

### 2. Open the Dashboard
Navigate to **`http://127.0.0.1:5000`** in your browser.

1. Fill out your profile (**Name**, **Age**, **Field**, **Interests**, **Skill Level**, and **Learning Style**).
2. Enter your **Learning Goal** (e.g., *"I want to master Python and Machine Learning"*).
3. Click **✨ Generate Recommendations**.
4. Review the personalized list of top 5 courses with match scores and rationales.
5. If desired, type feedback in the **Recommendation Feedback** box to refine and update the suggestions.

---

## 🌐 REST API Reference

### `POST /recommend`

Generates personalized recommendations based on the provided user profile.

#### Request Headers
```http
Content-Type: application/json
```

#### Request Body
```json
{
  "interests": "AI, Python",
  "skill_level": "Beginner",
  "learning_type": "Practical",
  "goal": "Become a machine learning engineer"
}
```

#### Response (200 OK)
```json
{
  "recommendations": [
    {
      "name": "Artificial Intelligence Fundamentals",
      "reason": "Matches your interest in Artificial Intelligence.",
      "score": 95
    },
    {
      "name": "Python Programming",
      "reason": "Matches your interest in Python programming.",
      "score": 95
    },
    {
      "name": "Machine Learning Basics",
      "reason": "Provides a foundation for learning AI.",
      "score": 92
    },
    {
      "name": "Python for Data Science",
      "reason": "Combines Python programming with data analysis.",
      "score": 91
    },
    {
      "name": "Generative AI",
      "reason": "Introduces modern AI and language-model concepts.",
      "score": 90
    }
  ]
}
```

---

## 🔄 Interactive Feedback Loop

The system features an active human-in-the-loop mechanism:
- When recommendations are displayed, a dedicated **Recommendation Feedback** card appears.
- If a user specifies adjustments (e.g., *"I want to focus more on Spring Boot and microservices"*), the client:
  1. Appends the new preference string into the existing interest vector.
  2. Issues a new asynchronous request to `/recommend`.
  3. Re-renders the updated curriculum options dynamically without page reloads.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
