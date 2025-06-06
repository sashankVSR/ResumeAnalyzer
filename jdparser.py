import nltk
nltk.download('punkt_tab') 
nltk.download('stopwords')  # Force download in case it's buggy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

def extract_keywords_from_jd(jd_text):
    tokens = word_tokenize(jd_text.lower())
    keywords = [word for word in tokens if word.isalpha() and word not in stop_words]
    return list(set(keywords))
