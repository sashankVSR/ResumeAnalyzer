import nltk
from nltk.tokenize import word_tokenize

# Ensure required NLTK data is downloaded (run once)
nltk.download('punkt_tab')

def calculate_ats_score(resume_text, job_keywords):
    # Tokenize resume text properly
    resume_words = set(word_tokenize(resume_text.lower()))
    # Keep only alphabetic tokens (filter out punctuation, numbers, etc.)
    resume_words = {word for word in resume_words if word.isalpha()}

    matched = resume_words.intersection(set(job_keywords))
    score = (len(matched) / len(job_keywords)) * 100 if job_keywords else 0

    return round(score, 2), list(matched), list(set(job_keywords) - matched)
