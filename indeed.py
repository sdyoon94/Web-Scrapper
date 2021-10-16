import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_page(url):  
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  total = int(soup.find(id="searchCountPages").text.strip().split()[2].replace(",","").replace("건",""))
  max_page = (total-1)//LIMIT + 1
  return min(max_page, 21)

def extract_job(html):
  title = html.find("span",title = True)["title"]
  company = html.find("span", {"class":"companyName"}).text
  location = html.find("div", {"class":"companyLocation"}).text
  job_id = html["data-jk"]
  return {"title": title, "company": company, "location": location, "link": f"https://kr.indeed.com/viewjob?jk={job_id}"}

def extract_jobs(last_page, url):
  jobs=[]
  for page in range(last_page):
    print(f"Scrapping Indeed : Page {page+1}")
    result = requests.get(f"{url}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a",{"class":"result"})
    for result in results:
      jobs.append(extract_job(result))
  return jobs

def get_jobs(word):
  url = f"https://kr.indeed.com/jobs?q={word}&limit={LIMIT}&filter=0"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs