from resume_parser import extract_resume_text
from text_cleaner import clean_text

raw_text = extract_resume_text("sample_resume.pdf")
cleaned_text = clean_text(raw_text)

print("RAW TEXT SAMPLE:")
print(raw_text[:300])

print("\nCLEANED TEXT SAMPLE:")
print(cleaned_text[:300])