# In resume_parser.py
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Takes a path to a PDF and returns its text."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

# --- This part is for testing the function directly ---
if __name__ == '__main__':
    # 1. Create a folder named 'resumes' in your project directory.
    # 2. Put a sample resume PDF inside it (e.g., 'sample.pdf').
    # 3. Change 'resumes/sample.pdf' to match your filename.
    sample_text = extract_text_from_pdf('resumes/sample.pdf')
    print("--- Extracted Resume Text ---")
    print(sample_text)