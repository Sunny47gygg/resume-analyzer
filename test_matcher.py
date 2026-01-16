from resume_parser import extract_resume_text
from text_cleaner import clean_text
from matcher import get_match_score

resume_text = extract_resume_text("sample_resume.pdf")
resume_clean = clean_text(resume_text)

job_description = """Looking for a Python Software Engineer with experience in backend development,
REST APIs, Django, performance optimization, and scalable systems.
"""

job_clean = clean_text(job_description)

print("RESUME CLEAN LENGTH:", len(resume_clean))
print("JOB CLEAN LENGTH:", len(job_clean))
print("RESUME CLEAN SAMPLE:", resume_clean[:200])
print("JOB CLEAN SAMPLE:", job_clean[:200])

score = get_match_score(resume_clean, job_clean)

print("Resume-Job Match Score: ", score, "%")