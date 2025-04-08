from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize GROQ LLM
groq_llm = ChatGroq(
    temperature=1.0,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)

def run_prompt(template_file: str, job_desc: str, resume_text: str) -> str:
    with open(template_file, "r") as file:
        prompt_template = PromptTemplate.from_template(file.read())
    chain = prompt_template | groq_llm
    return chain.invoke({"job": job_desc, "resume": resume_text})

def analyze_job_and_resume(job_desc, resume_text):
    return run_prompt("prompts/analyze_job.txt", job_desc, resume_text)

def improve_resume(resume_text, job_desc):
    return run_prompt("prompts/improve_resume.txt", job_desc, resume_text)

def generate_cover_letter(job_desc, resume_text):
    return run_prompt("prompts/cover_letter.txt", job_desc, resume_text)
