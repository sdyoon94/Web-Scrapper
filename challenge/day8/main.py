import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")

alba_url = "http://www.alba.co.kr"
alba_result = requests.get(alba_url)
alba_soup = BeautifulSoup(alba_result.text, "html.parser")
list_name = alba_soup.find("div", {"id":"MainSuperBrand"})
lists = list_name.find_all("li")
link = []
name = []
cant = '/\?%*:|"<>.'
for i in lists:
  try:
    link.append(i.find("a", {"class":"brandHover"})["href"])
    name.append((i.find("span",{"class":"company"})).string)
  except:
    pass

for i in range(len(link)):
  company_result = requests.get(link[i])
  company_soup = BeautifulSoup(company_result.text, "html.parser")
  try:
    count=int(company_soup.find("p",{"class":"jobCount"}).find("strong").string.replace(",",""))
  except:
    count=int(company_soup.find("p",{"class":"listCount"}).find("strong").string.replace(",",""))
  if count==0 : continue
  for j in range(len(cant)):
    name[i]=name[i].replace(cant[j],"_")
  file=open(f"{name[i]}.csv", mode="w")
  writer=csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  print(file)
  count-=1
  total_page = count//50 + 1
  for j in range(total_page):
    j+=1
    if"job/brand/" not in link[i]: link[i]+="job/brand/"
    job_url=f"{link[i]}?page={j}&pagesize=50"
    job_result=requests.get(job_url)
    job_soup=BeautifulSoup(job_result.text,"html.parser")
    tbody=job_soup.find("div",{"id":"NormalInfo"}).find("tbody")
    jobs=tbody.find_all("tr")

    for job in jobs:
      try:
        job_locale = job.find("td").get_text()
        job_company = job.find("span",{"class":"company"}).string.strip()
        job_time = job.find("td",{"class":"data"}).get_text()
        job_pay = job.find("td",{"class":"pay"}).get_text()
        job_reg = job.find("td",{"class":"regDate last"}).get_text()
        writer.writerow([job_locale, job_company, job_time, job_pay, job_reg])
      except:
        pass