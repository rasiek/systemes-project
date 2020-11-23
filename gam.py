import os
import json
import requests
from bs4 import BeautifulSoup

url="https://gamewave.fr/actualites/"
gsNews = requests.get(url)
soup = BeautifulSoup(gsNews.text, "lxml")

div = soup.find_all("div", {"class": "news"})
desc = soup.find_all("a", {"class": "href"})

liste_titre = [elt for elt in div]

liste_description = [elt for elt in desc]