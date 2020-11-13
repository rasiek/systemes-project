import requests
from bs4 import BeautifulSoup

url = "https://www.gamespot.com/news/"

try:
    gsNews = requests.get(url)
except Exception as e:
    print("Error:")
    print(e)
    print("\n")
    

if gsNews.status_code == 200:
    gsSoup = BeautifulSoup(gsNews.text, "lxml")

div_arts = gsSoup.find("div", attrs={"class": "horizontal-card-item"})

#Creating articles list from news page
as_links = []

as_links.append(div_arts.find("a", "horizontal-card-item__link").get("href"))

#Getting the link of each article
for i in div_arts.find_next_siblings():
    a = i.find("a", "horizontal-card-item__link")
    try:
        as_links.append(a.get("href"))
    except Exception as e:
        print(e)

urls_list = ["https://www.gamespot.com" + x for x in as_links]

for i in urls_list:
    print(i)


ej_url = urls_list[0]


try:
    art = requests.get(ej_url)
    if art.status_code == 200:
        soup_art = BeautifulSoup(art.text, "lxml")

        #Extract title
        title = soup_art.find("h1", attrs={"class": "news-title"}).get_text()
        print(title)

        #Extract Subtitle
        subTitle = soup_art.find("h2", attrs={"class": "news-deck"}).get_text()
        print(subTitle)

        #Extract article text
        art_text = soup_art.find("h2", attrs={"class": "news-deck"}).get_text()
        print(subTitle)


except Exception as identifier:
    pass

    

    

# for sib in div_arts.find_next_siblings():
#     link = sib.find("a", "horizontal-card-item__link").get("href")
#     as_links.append(link) 

# print(as_links)



