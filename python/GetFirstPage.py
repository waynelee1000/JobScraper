from bs4 import BeautifulSoup
import requests
import sys

sys.stdout = open("FirstPageScrape.txt", "w")

links = ['https://www.indeed.com/jobs?q=IT+intern&l=19107&sort=date','https://www.indeed.com/jobs?q=IT+intern&l=19107&sort=date&start=10']

for url in links:
    r = requests.get(url)

    soup = BeautifulSoup(r.content)

    for div in soup.find_all('div'):

        for title in div.find_all('h2'):

            if 'Intern' in title.text or 'intern' in title.text:
                

                for a in title.find_all('a', href=True):
                    jobURl = "https://www.indeed.com"+a.get('href')


                    """
                                        rJob = requests.get(jobURl)
                    jobSoup = BeautifulSoup(rJob.content)
                    
                    Inside td class =  snip 
                    Check for GPA requirement
                    If the TD class doesnt contain GPA allow
                    if GPA exist create another if statement to check value
                    """

                    for company in div.find_all('span',{'class': 'company'}):
                        

                        for date in div.find_all('span', {'class': 'date'}):
                            print(title.text)
                            print(jobURl)
                            print (company.text.lstrip())
                            print(date.text)
