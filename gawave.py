import requests
from bs4 import BeautifulSoup

url = "https://gamewave.fr/actualites/"
gmNews = requests.get(url)


if gmNews.ok:
    links= []
    gmNews = requests.get(url)
    gmSoup = BeautifulSoup(gmNews.text, "html.parser")
    div_arts = gmSoup.find("div", attrs={"class": "news"})
    for div in  div_arts:
        a = div.find('a')
        link = a['href']
        links.append("https://gamewave.fr/actualites/" + link)
    print(links)
