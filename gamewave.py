import requests
from bs4 import BeautifulSoup
url = "https://gamewave.fr/actualites/"


gmWave = requests.get(url)
print(gmWave.status_code)
if gmWave.status_code == 200:
    gmSoup = BeautifulSoup(gmWave.text, "lxml")

div_arts = gmSoup.find("div", attrs={"class": "infos"})

#Creating articles list from news page
as_links = []

as_links.append(div_arts.find("a", "news__link").get("href")
#Getting the link of each article
for i in div_arts.find_next_siblings():
    a = i.find("a", "news__link")
    try:
        as_links.append(a.get("href"))
    except Exception as e:
        print(e)

urls_list = ["https://gamewave.fr/actualites/" + x for x in as_links]

for i in urls_list:
    print(i)

ej_url = urls_list[13]

try:
    art = requests.get(ej_url)
    if art.status_code == 200:
        soup_art = BeautifulSoup(art.text, "lxml")

        #Extract title 

        title = soup_art.find("h1", attrs={"class": "infos-title"}).get_text()
        print(title)
        #Extract Subtitle
        subTitle = soup_art.find("h2", attrs={"class": "infos"}).get_text()
        print(subTitle)

        #Extract article text
        art_text = soup_art.find("a", attrs={"class": "intro"}).get_text()
        print(subTitle)


except Exception as identifier:
    pass
