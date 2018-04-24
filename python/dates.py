from bs4 import BeautifulSoup
import requests
import sys


r = requests.get("https://www.indeed.com/q-IT-intern-l-19107-jobs.html")
sys.stdout = open("dates.txt", "w")

soup = BeautifulSoup(r.content)

for link in soup.find_all('span', {'class': 'date'}):
    print(link.text)
    




