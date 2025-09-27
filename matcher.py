# In matcher.py

# ==============================================================================
# 1. IMPORTS - All necessary libraries are imported once at the top.
# ==============================================================================
import os
import re
import time
import nltk
import spacy
from collections import defaultdict
from datetime import datetime
from googlesearch import search
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import language_tool_python

# ==============================================================================
# 2. INITIALIZATION - Load models and tools once when the app starts.
# ==============================================================================

# --- NLTK setup: Corrected error handling ---
# --- NLTK setup: Checks for all required packages ---
REQUIRED_PACKAGES = ['punkt', 'punkt_tab']
for package in REQUIRED_PACKAGES:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        print(f"Downloading NLTK's '{package}' model...")
        nltk.download(package, quiet=True)
# --- End of NLTK setup ---

# --- Load AI Models ---
print("Loading AI models, this may take a moment...")
SENTENCE_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
SUMMARIZER = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
LANGUAGE_TOOL = language_tool_python.LanguageTool('en-US')
CUSTOM_NER_MODEL_PATH = "./output/model-best"
CUSTOM_NLP = None
if os.path.exists(CUSTOM_NER_MODEL_PATH):
    CUSTOM_NLP = spacy.load(CUSTOM_NER_MODEL_PATH)
    print("Custom NER model loaded successfully.")
else:
    print("Warning: Custom NER model not found. Entity extraction will be skipped.")

print("Models loaded.")

# ==============================================================================
# 3. FUNCTIONS - All our features, each defined once.
# ==============================================================================

def calculate_similarity(text1, text2):
    """Calculates the semantic similarity between two full texts."""
    if not text1 or not text2:
        return 0.0
    embedding1 = SENTENCE_MODEL.encode(text1, convert_to_tensor=True)
    embedding2 = SENTENCE_MODEL.encode(text2, convert_to_tensor=True)
    cosine_scores = util.cos_sim(embedding1, embedding2)
    score = cosine_scores.item() * 100
    return round(score, 2)

def find_most_similar_sentences(resume_text, job_desc_text, top_n=3):
    """Finds the top N sentences in the resume that are most similar to the job description."""
    if not resume_text or not job_desc_text:
        return []
    resume_sentences = nltk.sent_tokenize(resume_text)
    job_desc_embedding = SENTENCE_MODEL.encode(job_desc_text, convert_to_tensor=True)
    resume_embeddings = SENTENCE_MODEL.encode(resume_sentences, convert_to_tensor=True)
    cosine_scores = util.cos_sim(resume_embeddings, job_desc_embedding)
    top_results = cosine_scores.flatten().topk(k=min(top_n, len(resume_sentences)))
    highlighted_sentences = [resume_sentences[i] for i in top_results.indices]
    return highlighted_sentences

def extract_years_of_experience(text):
    """Extracts an estimated years of experience from resume text."""
    year_pattern = re.compile(r'\b(19[8-9]\d|20[0-2]\d)\b')
    years = [int(y) for y in year_pattern.findall(text)]
    if not years:
        return "Not found"
    earliest_year = min(years)
    latest_year = max(years)
    if re.search(r'present|current', text, re.IGNORECASE):
        latest_year = datetime.now().year
    experience_years = latest_year - earliest_year
    return max(0, experience_years)

def check_ats_friendliness(text):
    """Checks for basic ATS-friendly characteristics and returns recommendations."""
    recommendations = []
    if not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        recommendations.append("❌ No email address found. Ensure your contact info is clear and readable.")
    else:
        recommendations.append("✅ Contact information detected.")
    if not re.search(r'skills', text, re.IGNORECASE):
        recommendations.append("❌ A dedicated 'Skills' section was not found. Consider adding one for better keyword matching.")
    else:
        recommendations.append("✅ 'Skills' section detected.")
    if not re.search(r'experience|history', text, re.IGNORECASE):
        recommendations.append("❌ A clear 'Work Experience' or 'Work History' section was not found.")
    else:
        recommendations.append("✅ 'Experience' section detected.")
    return recommendations

def summarize_resume(text):
    """Generates a summary for the given text."""
    if len(text.split()) < 50:
        return "Resume is too short to summarize."
    try:
        summary = SUMMARIZER(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Could not generate summary: {e}"

def check_grammar_and_spelling(text):
    """Checks for grammar and spelling errors and returns a summary."""
    try:
        matches = LANGUAGE_TOOL.check(text)
        error_count = len(matches)
        if error_count == 0:
            return "✅ No significant spelling or grammar errors found."
        else:
            return f"❌ Found {error_count} potential spelling or grammar errors."
    except Exception as e:
        return f"Could not perform grammar check: {e}"

def infer_skill_proficiency(text):
    """Infers skill proficiency based on contextual keywords."""
    expert_keywords = ['led', 'architected', 'managed', 'developed', 'built', 'implemented', 'optimized']
    familiar_keywords = ['assisted', 'supported', 'contributed', 'worked with', 'familiar with']
    skills_to_find = ['python', 'java', 'sql', 'react', 'aws', 'docker', 'git', 'machine learning', 'nlp']
    found_skills = {"Expert": set(), "Familiar": set()}
    sentences = nltk.sent_tokenize(text.lower())
    for sentence in sentences:
        for skill in skills_to_find:
            if skill in sentence:
                if any(verb in sentence for verb in expert_keywords):
                    found_skills["Expert"].add(skill.title())
                elif skill.title() not in found_skills["Expert"] and any(verb in sentence for verb in familiar_keywords):
                    found_skills["Familiar"].add(skill.title())
    return {"Expert": sorted(list(found_skills["Expert"])), "Familiar": sorted(list(found_skills["Familiar"]))}

def check_for_plagiarism(text):
    """Selects key sentences and searches for them online to detect plagiarism."""
    plagiarized_sentences = []
    sentences = nltk.sent_tokenize(text)
    sentences_to_check = [s for s in sentences if 8 < len(s.split()) < 30][:3]
    if not sentences_to_check:
        return {"status": "✅ No scannable sentences found.", "sentences": []}
    for sentence in sentences_to_check:
        try:
            query = f'"{sentence}"'
            results = list(search(query, num=3, stop=3, pause=1.0))
            if len(results) > 1:
                plagiarized_sentences.append(sentence)
        except Exception as e:
            print(f"Could not perform search: {e}")
            return {"status": "⚠️ Search could not be completed.", "sentences": []}
    if plagiarized_sentences:
        return {"status": f"❌ Found {len(plagiarized_sentences)} sentence(s) that may not be original.", "sentences": plagiarized_sentences}
    else:
        return {"status": "✅ Content appears to be original.", "sentences": []}

def extract_custom_entities(text):
    """Loads the custom-trained model and extracts entities."""
    if not CUSTOM_NLP:
        return {"error": "Custom model not loaded."}
    doc = CUSTOM_NLP(text)
    entities = defaultdict(list)
    for ent in doc.ents:
        if ent.text not in entities[ent.label_]:
            entities[ent.label_].append(ent.text)
    return dict(entities)