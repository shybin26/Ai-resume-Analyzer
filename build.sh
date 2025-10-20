#!/usr/bin/env bash
# exit on error
set -o errexit

echo "--- Installing Dependencies ---"
pip install -r requirements.txt

echo "--- Downloading AI/NLP Models ---"
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

echo "--- Training Custom NER Model ---"
python prepare_data.py
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy

echo "--- Running Database Migrations ---"
flask db upgrade

echo "--- Build Complete ---"