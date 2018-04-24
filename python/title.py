from bs4 import BeautifulSoup
import requests
import sys


r = requests.get("https://www.indeed.com/jobs?q=IT+intern&l=19107&sort=date")
sys.stdout = open("title.txt", "w")

soup = BeautifulSoup(r.content)

div = soup.find('div')

title = div.find('h2')


date = soup.find('span', {'class': 'date'})

for div in soup.find_all('div'):

    for title in div.find_all('h2'):
        print(title.text)

        for a in title.find_all('a', href=True):
            print("https://www.indeed.com"+a.get('href'))

    for company in div.find_all('span',{'class': 'company'}):
            print (company.text.lstrip())


    for date in div.find_all('span', {'class': 'date'}):
    		print(date.text)


