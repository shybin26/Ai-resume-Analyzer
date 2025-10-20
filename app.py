# In app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json 
from datetime import datetime

# --- This is the corrected import line ---
from matcher import (
    calculate_similarity, find_most_similar_sentences, 
    extract_years_of_experience, check_ats_friendliness, 
    summarize_resume, check_grammar_and_spelling, 
    infer_skill_proficiency, check_for_plagiarism, extract_custom_entities
)
from resume_parser import extract_text_from_pdf

app = Flask(__name__)

# --- NEW: PostgreSQL Database Configuration ---
# The DATABASE_URL is provided by Render. It falls back to a local SQLite
# database if the variable isn't found (for local testing).
database_url = os.environ.get('DATABASE_URL', 'sqlite:///analysis_history.db')

# Heroku/Render use 'postgres://' but SQLAlchemy needs 'postgresql://'
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# --- End of Database Model ---


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/history')
def history():
    all_analyses = Analysis.query.order_by(Analysis.timestamp.desc()).all()
    return render_template('history.html', analyses=all_analyses)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file provided"}), 400
    
    resume_file = request.files['resume']
    job_description = request.form.get('jd', '')
    
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, resume_file.filename)
    resume_file.save(file_path)
    
    resume_text = extract_text_from_pdf(file_path)
    
    # --- Execute all analysis tasks ---
    results_data = {
        "score": calculate_similarity(resume_text, job_description),
        "experience": extract_years_of_experience(resume_text),
        "summary": summarize_resume(resume_text),
        "highlights": find_most_similar_sentences(resume_text, job_description),
        "ats_tips": check_ats_friendliness(resume_text),
        "grammar_report": check_grammar_and_spelling(resume_text),
        "inferred_skills": infer_skill_proficiency(resume_text),
        "plagiarism_report": check_for_plagiarism(resume_text),
        "custom_entities": extract_custom_entities(resume_text),
        "full_resume_text": resume_text
    }
    
    os.remove(file_path)

    # --- Save results to the database ---
    try:
        new_analysis = Analysis(
            resume_filename=resume_file.filename,
            score=results_data.get('score', 0),
            full_report_json=json.dumps(results_data)
        )
        db.session.add(new_analysis)
        db.session.commit()
    except Exception as e:
        print(f"Database save error: {e}")
        db.session.rollback()
    
    return jsonify(results_data)

if __name__ == '__main__':
    app.run(debug=True)