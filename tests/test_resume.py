from resume_parser import extract_resume_text

text = extract_resume_text("sample_resume.pdf")
print("========RESULT=======")
print("TEXT LENGTH:", len(text))
if len(text) == 0:
    print("no extractable text")
else:
    print(text[:500])