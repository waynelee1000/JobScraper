from bs4 import BeautifulSoup
import requests
import sys

sys.stdout = open("SecondPageScrape.txt", "w")

links = ['https://www.indeed.com/jobs?q=IT+intern&l=19107&sort=date','https://www.indeed.com/jobs?q=IT+intern&l=19107&sort=date&start=10']

companyText = ""
titleText = ""
urlText = ""
dateText = ""
caseInfo = ""
case = False


for url in links:
    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    for div in soup.find_all('div'):

        for title in div.find_all('h2'):

            if 'IT' in title.text:
                titleText = title.text

                for a in title.find_all('a', href=True):
                    jobURl = "https://www.indeed.com"+a.get('href')

                    urlText = jobURl

                    rJob = requests.get(jobURl)
                    jobSoup = BeautifulSoup(rJob.content)

                    for ul in jobSoup.find_all('ul'):
                        for li in ul.find_all('li'):
                            if 'Word' in li.text:
                                caseInfo = li.text
                                case = True

                    for company in div.find_all('span',{'class': 'company'}):
                        companyText = company.text.lstrip()   

                    for date in div.find_all('span', {'class': 'date'}):
                        dateText = date.text
                        if case == True:
                            print (titleText)
                            print (companyText)
                            print (urlText)
                            print (caseInfo)
                            print (dateText)
