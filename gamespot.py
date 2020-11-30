import requests
from bs4 import BeautifulSoup
import sqlite3
from app import functions as fc



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

title_list = []
subt_list = []
a_text_list = []
author_list = []
date_list = []

for url in urls_list:
    try:
        art = requests.get(url)
        if art.status_code == 200:
            soup_art = BeautifulSoup(art.text, "lxml")

            #Extract title
            title = soup_art.find("h1", attrs={"class": "news-title"}).get_text()
            print(title)
            # title_list.append(title)

            #Extract Subtitle
            subTitle = soup_art.find("h2", attrs={"class": "news-deck"}).get_text()
            print(subTitle)
            # subt_list.append(subTitle)

            #Extract article text
            # art_text = soup_art.find("div", attrs={"class": "content-entity-bdy"})

            author = soup_art.find("a", "byline-author__name").get_text()
            # author_list.append(author)

            art_text = soup_art.find("div", attrs={"class": "js-content-entity-body"}).find_all("p")

            textString = ""

            for e in art_text:
                textString += e.get_text() + "\n"

            print(textString)

            fc.insertQuery(title, subTitle, url, textString)
            
            # a_text_list.append(textString)

            #Extract author

            #Extract date
            # date_art = soup_art.find("time", attrs={"pubtime": "pubtime"}).get("datetime")
            # date_list.append(date_art)

    except:
        pass

