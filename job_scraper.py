import requests
from bs4 import BeautifulSoup
import pandas as pd 




def extract(page):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"}
    url =  f"https://web3.career/marketing+remote-jobs?page={page}"
    r = requests.get(url,headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup






def transform(soup):
    divs = soup.find_all('div', class_="d-flex align-middle")
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('div', class_="mt-auto d-block d-md-flex").text.strip()
        try:
            salary = item.find('p', class_="text-salary").text.strip()
        except:
            salary = ''
        job = {
            "title":title,
            "company":company,
            "salary":salary
        }
        joblist.append(job)
    return



joblist = []
#class="d-flex align-middle"


for i in range(1,5):
    print(f'Getting page {i}')
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
    
print(df.head())

df.to_csv("jobs.csv")