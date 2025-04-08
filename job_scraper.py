import requests
from bs4 import BeautifulSoup

def scrape_linkedin_jobs(keyword, location="Remote", max_jobs=5):
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all('div', class_='base-card'):
        if len(jobs) >= max_jobs:
            break
        title = job_card.find('h3').text.strip() if job_card.find('h3') else "N/A"
        company = job_card.find('h4').text.strip() if job_card.find('h4') else "N/A"
        link = job_card.find('a')['href'] if job_card.find('a') else "N/A"
        jobs.append({
            "title": title,
            "company": company,
            "link": link
        })
    return jobs
