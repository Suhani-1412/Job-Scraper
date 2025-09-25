from bs4 import BeautifulSoup
import requests
import time

# Dates you want to allow
allowed_date=['1 days','2 days','3 days']

# Take unfamiliar skills from user
print("Put some unfamiliar skills comma seperated")
unfamilar_skills=input(">").lower().split(',')
unfamilar_skills=[s.strip() for s in unfamilar_skills]
print(f"Filtering out unfamiliar skills {unfamilar_skills}")


def find_jobs():
    html=requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python&cboWorkExp1=-1&txtLocation=").text

    try:    
        soup = BeautifulSoup(html, "lxml")   #its kind of crashing in first go and when i run it second tym its working so i used try and except
    except Exception:   
        soup = BeautifulSoup(html, "html.parser")
    jobs=soup.find_all('li')
    for index,job in enumerate(jobs):
        title=job.find('span',class_='srp-comp-name')
        skills=job.find('div',class_='srp-keyskills')
        published_date=job.find('span',class_="posting-time")
        link=job.find('div',class_='srp-listing')
        if title and skills and published_date and link:  # check all exist
            published_date = published_date.text.strip()
            if any(date in published_date for date in allowed_date):
                if not any( unfskills in skills.text.lower() for unfskills in unfamilar_skills):
                    with open(f'post/{index}.txt','w')as f:
                        f.write(f"Company-->{title.text.strip()},\nSkills-->{skills.text.strip()}\n")
                        f.write(f"Link-->{link.a['href']}\n")
                    
           
if __name__ =='__main__':
    while True:
        find_jobs()
        waitTime=10
        print(f"waiting {waitTime}minutes......")
        time.sleep(waitTime*60)  #every 10 mins
        
        
    
    
  
