import pandas as pd
import requests
from bs4 import BeautifulSoup, SoupStrainer
import wget
import os

os.chdir("raw")

domain = "https://www.ons.gov.uk"
links = []

url = "https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata/2021"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for link in soup.find_all("a"):
    links.append(link.get("href"))

files = [domain + n for n in links if "xlsx" in n]

latest_week = files[0]

os.system(f"wget -O {latest_week[latest_week.rfind('/')+1:]} {latest_week}")
