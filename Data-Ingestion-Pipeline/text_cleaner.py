import re

def clean_text(text: str) -> str:
    """
    Normalize text & remove basic PII (emails, phones, card numbers).
    For production, replace with Presidio or SpaCy NER for stronger PII detection.
    """
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    # Remove common PII patterns
    text = re.sub(r"\b[\w._%+-]+@[\w.-]+\.\w{2,}\b", "[EMAIL]", text)  # emails
    text = re.sub(r"\b\d{10,16}\b", "[NUMBER]", text)  # phone/credit card numbers
    text = re.sub(r"\b\d{3}[-.\s]?\d{2}[-.\s]?\d{4}\b", "[ID]", text)  # SSN-like patterns
    return text
