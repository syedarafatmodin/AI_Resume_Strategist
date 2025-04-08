from langchain_groq import ChatGroq
from job_scraper import scrape_linkedin_jobs
from resume_parser import extract_text_from_pdf
from agent import analyze_job_and_resume, improve_resume, generate_cover_letter

resume_text = extract_text_from_pdf("sample_resume.pdf")  # or use extract_text_from_docx()

jobs = scrape_linkedin_jobs("AI Engineer")

for job in jobs:
    print(f"\n🔍 Job: {job['title']} at {job['company']}")
    
    # In a real app, you'd scrape full job description from job['link']
    job_desc = f"This is a sample job description for {job['title']} at {job['company']}."

    print("\n📊 Analysis:")
    print(analyze_job_and_resume(job_desc, resume_text))

    print("\n📌 Resume Improvement Suggestions:")
    print(improve_resume(resume_text, job_desc))

    print("\n📝 Cover Letter:")
    print(generate_cover_letter(job_desc, resume_text))
