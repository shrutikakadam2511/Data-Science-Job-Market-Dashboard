import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs(query="data science", pages=2):
    jobs = []

    for page in range(pages):
        url = f"https://www.indeed.com/jobs?q={query}&start={page*10}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        for card in soup.select("div.job_seen_beacon"):
            title = card.find("h2", class_="jobTitle").text.strip()
            company = card.find("span", class_="companyName")
            location = card.find("div", class_="companyLocation")
            summary = card.find("div", class_="job-snippet")

            jobs.append({
                "title": title,
                "company": company.text.strip() if company else None,
                "location": location.text.strip() if location else None,
                "summary": summary.text.strip() if summary else None
            })

    df = pd.DataFrame(jobs)
    df.to_csv("jobs.csv", index=False)
    return df

# Example usage
# scrape_jobs()
