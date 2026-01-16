import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

def generate_resume_suggestions(resume_text, job_text, missing_skills):
    prompt = f"""
You are an AI career assistant.

Resume text:
{resume_text[:1500]}

Job description:
{job_text[:1500]}

Missing skills:
{", ".join(missing_skills)}

Task:
Give 2-3 concise, actionable suggestion to improve the resume
so it better matches the job description.
"""
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature = 0.5
    )

    return response.choices[0].message.content