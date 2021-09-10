import pandas as pd
import requests
from bs4 import BeautifulSoup, SoupStrainer
import wget
import os

os.chdir("raw")

domain = "https://www.ons.gov.uk"
links = []

url = "https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata/2020"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for link in soup.find_all("a"):
    links.append(link.get("href"))

url = "https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata/2021"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for link in soup.find_all("a"):
    links.append(link.get("href"))

files = [domain + n for n in links if "xlsx" in n]

for url in files:
    # print(url)
    # print(url[url.rfind('/')+1:])
    os.system(f"wget -O {url[url.rfind('/')+1:]} {url}")
