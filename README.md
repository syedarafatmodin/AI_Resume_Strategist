# 🤖 AI-Powered Resume Strategist Agent

An intelligent agent that reads your resume, scrapes job descriptions from LinkedIn, performs a comparative analysis, and generates actionable insights to boost your job applications.

## 🔍 Overview

The Resume Strategist Agent helps job seekers optimize their resume for specific roles by leveraging AI and automation. It performs:

- 📄 **Resume Parsing** (from PDF)
- 🌐 **Job Description Scraping** (from LinkedIn)
- 📊 **Resume vs. JD Analysis**
- ✅ **Skills Gap Identification**
- 💡 **Improvement Suggestions**
- ✍️ **Tailored Cover Letter Generation**

---

## 🚀 Features

- Upload a resume (PDF format)
- Input job title, company name, or location
- Automatically scrapes matching job listings from LinkedIn
- Uses LLM (e.g., GPT/Groq) to:
  - Compare your resume with job descriptions
  - Highlight missing skills or keywords
  - Suggest resume improvements
  - Generate a personalized cover letter

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Frontend Interface
- **LangChain** – LLM Orchestration
- **GROQ / OpenAI API** – Language Model
- **BeautifulSoup / Playwright / Selenium** – Web Scraping
- **PyMuPDF / pdfplumber** – Resume Parsing
- **dotenv** – Environment Variable Management

---

## 📁 Project Structure

```
resume-strategist-agent/
│
├── frontend.py              # Streamlit UI
├── resume_parser.py         # PDF parsing logic
├── job_scraper.py           # LinkedIn job scraping
├── resume_analyzer.py       # Skill gap + matching logic
├── cover_letter_generator.py# LLM-powered cover letter
├── utils/                   # Helper functions/utilities
├── .env                     # API keys (not pushed to GitHub)
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/resume-strategist-agent.git
cd resume-strategist-agent
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your API keys**

Create a `.env` file in the root directory with the following:

```env
OPENAI_API_KEY=your-key-here
GROQ_API_KEY=your-key-here
TAVILY_API_KEY=your-key-here
```

5. **Run the app**

```bash
streamlit run frontend.py
```

---

## 📸 Demo Screenshots

*Coming soon – Include screenshots or a Loom video here!*

---

## 🧠 Future Improvements

- Upload DOCX resumes
- Support multiple job sources (Indeed, Glassdoor)
- More advanced analytics (match score, ranking)
- Resume versioning & PDF export
- User authentication

---

## 🤝 Contributing

Feel free to open issues or submit pull requests. All contributions are welcome!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 📬 Contact

Built by [Syed Arafat Modin] www.linkedin.com/in/syed-arafat-modin-580156120



DM me on LinkedIn or raise an issue if you’d like to collaborate or need help!

```

---
