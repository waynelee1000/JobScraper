from bs4 import BeautifulSoup
import requests
import sys


r = requests.get("https://www.indeed.com/jobs?q=IT+intern&l=19107&start=10")
sys.stdout = open("div.txt", "w")

soup = BeautifulSoup(r.content)
for div in soup.select("div.result > div:nth-of-type(1)"):
	print (div.text)
