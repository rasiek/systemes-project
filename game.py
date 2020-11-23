
import requests
from bs4 import BeautifulSoup
import json
import sys
url = "https://gamewave.fr/actualites/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

news = soup.find_all("div ", {"class: news"})


for x in news:
    article = x.find("a").text






#----------recuperer le texte des articles-------------------------------------



url3 ="https://gamewave.fr/les-sims-4/les-sims-4-escapade-enneigee-decouvrez-le-monde-de-mont-komorebi/"
r2= requests.get(url3)
soup2 = BeautifulSoup(r2.text,"html.parser")

article = soup2.find("div", {"class": "left"}).text

print(article)




url4 = "https://gamewave.fr/godfall/godfall-la-reelle-tombee-des-dieux/"
r3 = requests.get(url4)
soup3= BeautifulSoup(r3.text, "html.parser")

article =soup3.find("div",{"class":"left"}).text

print(article)


url12= "https://gamewave.fr/pokemon-epee-et-bouclier/pokemon-epee-et-bouclier-comment-recuperer-zarude/"
r1= requests.get(url12)
soup1 = BeautifulSoup(r1.text, "html.parser")

article = soup1.find("div", {"class" : "left"}).text

print(article)



