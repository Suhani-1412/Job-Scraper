# Job-Scraper
A Python-based job scraper that filters job postings from TimesJobs using BeautifulSoup and requests. Built as a learning project to practice web scraping, filtering, and file handling.

📌Features
Scrapes Python-related jobs from TimesJobs.
Filters jobs by posting date (1 day, 2 days, 3 days).
Excludes jobs with unfamiliar skills (provided by user input).
Saves job details into post/ folder as .txt files.
Runs in a loop and refreshes every 10 minutes (configurable).

🛠️ Tech Stack
Python 3
Requests – fetch HTML
BeautifulSoup (bs4) – parse HTML
lxml – fast parser

📂 Project Structure
job-scraper/
│── scraper.py         # main script
│── post/              # scraped job postings (auto-generated)
│── requirements.txt   # dependencies
│── README.md          # documentation

⚡ How It Works
User enters unfamiliar skills (comma-separated).
Example:
Put some unfamiliar skills comma separated
> java, php

→ The script will skip any job that mentions Java or PHP.
The scraper fetches jobs from TimesJobs.
Filters by allowed dates (1 days, 2 days, 3 days).
Saves matching job details into post/0.txt, post/1.txt, etc.
Each file contains:

Company --> XYZ Pvt Ltd
Skills --> Python, Django, SQL
Link --> https://timesjobs.com/jobdetail/...

🚀 How to Run
Clone the repo:

git clone https://github.com/Suhani-1412/job-scraper.git
cd job-scraper

Create virtual environment & install dependencies:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

Run the script:
python scraper.py

📦 Requirements
Create a requirements.txt file with:
beautifulsoup4
lxml
requests

📝Future Improvements
Save results in CSV instead of multiple text files.
Add email notification when new jobs are found.
Integrate with a database (SQLite/MongoDB).
