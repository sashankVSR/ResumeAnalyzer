import streamlit as st
from utils.pdfparser import extract_text_from_pdf
from utils.jdparser import extract_keywords_from_jd
from utils.atsscoreparser import calculate_ats_score

st.title("📄 Resume Analyzer & ATS Scorer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the Job Description here")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    job_keywords = extract_keywords_from_jd(job_description)
    
    ats_score, matched, missing = calculate_ats_score(resume_text, job_keywords)

    st.subheader(f"✅ ATS Score: {ats_score}%")
    st.write("✅ Matched Keywords:", matched)
    st.write("❌ Missing Keywords:", missing)

    st.subheader("📌 Suggestions:")
    for kw in missing:
        st.write(f"• Consider adding the skill: **{kw}**")
