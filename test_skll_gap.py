from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_gap import get_skill_gap

resume_text = extract_resume_text("sample_resume.pdf")
resume_clean = clean_text(resume_text)

job_description = """
Looking for a Python Software Engineer with experience in backned development,
REST APIs, Django, aws, docker and performance optimization, and scalable systems.
"""
job_clean = clean_text(job_description)

gap = get_skill_gap(resume_clean, job_clean)

print("MATCHED SKILLS:", gap["matched_skills"])
print("\nMISSING SKILLS:", gap["missing_skills"])