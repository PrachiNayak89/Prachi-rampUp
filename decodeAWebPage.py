#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

url='https://www.nytimes.com/'

req=requests.get(url)
sourceCode=req.text

soup = BeautifulSoup(sourceCode)

for headings in soup.find_all(class_="story-heading"):
    if headings.a:
        print(headings.a.text.replace("\n"," ").strip())
    else:
        print(headings.contents[0].strip())
