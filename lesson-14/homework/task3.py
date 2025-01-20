import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Database setup
def setup_database():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            location TEXT NOT NULL,
            job_description TEXT,
            application_link TEXT,
            UNIQUE(job_title, company_name, location)
        )
    ''')
    conn.commit()
    return conn

# Scrape job listings from the website
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all('div', class_='card-content'):
        job_title = job_card.find('h2', class_='title').text.strip()
        company_name = job_card.find('h3', class_='subtitle').text.strip()
        location = job_card.find('p', class_='location').text.strip()
        job_description = job_card.find('div', class_='content').text.strip()
        application_link = job_card.find('a', text='Apply')['href']
        jobs.append((job_title, company_name, location, job_description, application_link))

    return jobs

# Insert or update job listings in the database
def store_jobs(conn, jobs):
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute('''
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(job_title, company_name, location) DO UPDATE SET
                job_description = excluded.job_description,
                application_link = excluded.application_link
        ''', job)
    conn.commit()

# Filter job listings by location or company name
def filter_jobs(conn, location=None, company_name=None):
    cursor = conn.cursor()
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location = ?"
        params.append(location)
    if company_name:
        query += " AND company_name = ?"
        params.append(company_name)

    cursor.execute(query, params)
    return cursor.fetchall()

# Export filtered results to a CSV file
def export_to_csv(jobs, filename="filtered_jobs.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
        writer.writerows(jobs)

if __name__ == "__main__":
    # Setup database
    conn = setup_database()

    # Scrape and store jobs
    jobs = scrape_jobs()
    store_jobs(conn, jobs)

    # Example: Filter by location or company name
    filtered_jobs = filter_jobs(conn, location="Remote")
    print("Filtered Jobs:", filtered_jobs)

    # Export filtered jobs to CSV
    export_to_csv(filtered_jobs)

    conn.close()
