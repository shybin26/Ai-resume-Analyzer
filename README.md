# AI Resume Analyzer 🚀

This is a full-stack web application designed to provide an in-depth, AI-powered analysis of resumes against job descriptions. The tool leverages a suite of advanced Natural Language Processing (NLP) models to extract meaningful insights, score semantic similarity, and provide actionable feedback.

---

## ✨ Key Features

* **🧠 Semantic Match Scoring:** Goes beyond simple keywords to understand the contextual meaning of the resume and job description.
* **🤖 Custom Entity Recognition (NER):** Powered by a custom-trained spaCy model to identify specific skills, software, and certifications.
* **📝 AI-Generated Summarization:** Utilizes a generative transformer model to create a concise summary of the candidate's profile.
* **📊 Detailed Reporting:** Generates a comprehensive report, including:
    * **Years of Experience Extraction**
    * **Skill Proficiency Inference**
    * **ATS & Writing Analysis** (Grammar, Spelling, Key Sections)
    * **Plagiarism Detection**
* **🎨 Dynamic UI:** A modern, single-page application (SPA) interface with sentence highlighting.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Migrate
* **AI/NLP:** spaCy, Transformers (Hugging Face), Sentence-Transformers, NLTK
* **Database:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
