import streamlit as st

from suggestions import generate_resume_suggestions
from resume_parser import extract_resume_text
from text_cleaner import clean_text
from matcher import get_match_score
from skill_gap import get_skill_gap

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer & Job Matcher")
st.write("Upload your resume and paste the job description")

if "ai_suggestions" not in st.session_state:
    st.session_state.ai_suggestions = None

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

#Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

#Job Description input
job_description = st.text_area("Paste Job Description")

analyze_clicked = st.button("Analyze Resume")

if analyze_clicked and uploaded_file and job_description:
    st.session_state.ai_suggestions = None
    st.session_state.analyzed = False

    with st.spinner("Analyzing resume..."):

        resume_text = extract_resume_text(uploaded_file)
        resume_clean = clean_text(resume_text)

        job_clean = clean_text(job_description)

        score = get_match_score(resume_clean, job_clean)
        gap = get_skill_gap(resume_clean, job_clean)

        st.session_state.resume_text = resume_text
        st.session_state.job_description = job_description
        st.session_state.gap = gap
        st.session_state.score = score

        st.session_state.analyzed = True

#Results section

if st.session_state.analyzed:
    st.subheader("Results")

    col1, col2, col3 = st.columns(3)
    col1.metric("Resume-Job Match", f"{st.session_state.score*10}%")
    col2.metric("Matched Skills", len(st.session_state.gap["matched_skills"]))
    col3.metric("Missing Skills", len(st.session_state.gap["missing_skills"]))

    st.subheader("Matched Skills")
    st.write(", ".join(st.session_state.gap["matched_skills"]) or "None")

    st.subheader("Missing Skills")
    st.write(", ".join(st.session_state.gap["missing_skills"]) or "None")

    #AI Suggestions button

    if st.button("Generate Suggestions"):
        with st.spinner("Generating AI-powered resume suggestions..."):
            st.session_state.ai_suggestions = generate_resume_suggestions(
                st.session_state.resume_text,
                st.session_state.job_description,
                st.session_state.gap["missing_skills"]
            )

    if st.session_state.ai_suggestions:
        st.subheader("Resume Suggestions")
        st.write(st.session_state.ai_suggestions)


elif analyze_clicked:
    st.warning("Please upload a resume and paste a job description.")