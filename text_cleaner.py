import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))

def clean_text(text):
    #convert to lower
    text = text.lower()

    #remove special chars and numbers
    text = re.sub(r'[^a-zA-Z ]',' ', text)

    #remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    #remove standalone numbers
    text = re.sub(r'\b\d+\b', ' ', text)

    return text