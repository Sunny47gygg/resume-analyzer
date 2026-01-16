from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_match_score(resume_text, job_text):
    if not resume_text.strip() or not job_text.strip():
        return 0.0
    
    vectorizer = TfidfVectorizer(
        ngram_range=(1,2),
        min_df=1,
        token_pattern=r'(?u)\b[a-zA-Z]{2,}\b'
    )

    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0], vectors[1])

    return round(similarity[0][0] * 100,2)