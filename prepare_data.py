# In prepare_data.py
import spacy
from spacy.tokens import DocBin

# Import the training data you created
from training_data import TRAIN_DATA

# Create a blank English model. We only need the tokenizer for this.
nlp = spacy.blank("en")

# DocBin is a container for spaCy's Doc objects.
doc_bin = DocBin()

print("Starting data preparation...")

# Iterate through your training examples
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    ents = []

    # Create Span objects for each entity
    for start, end, label in annotations.get("entities"):
        span = doc.char_span(start, end, label=label)
        if span is None:
            # This will warn you if the character indices don't align with tokens
            print(f"Skipping entity: Cannot create span for text '{text[start:end]}' in '{text}'")
        else:
            ents.append(span)

    # Assign the collected spans to the document's entities
    try:
        doc.ents = ents
        doc_bin.add(doc)
    except ValueError:
        print(f"Skipping doc due to overlapping entities: '{text}'")


# Save the DocBin to a .spacy file
output_path = "./train.spacy"
doc_bin.to_disk(output_path)

print(f"✅ Data preparation complete! Output file: {output_path}")