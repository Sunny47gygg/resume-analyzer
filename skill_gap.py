from skill_extractor import extract_skills

def get_skill_gap(resume_text, job_text):
    resume_words = extract_skills(resume_text)
    job_words = extract_skills(job_text)

    missing_skills = job_words - resume_words
    matched_skills = job_words & resume_words

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }