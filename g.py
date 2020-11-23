import requests

from bs4 import BeautifulSoup

url = "https://gamewave.fr/actualites/"
try:
     gmNews = requests.get(url)
except Exception as o:
     print("Error:")
     print(o)
     print("\n")
if gmNews.status_code ==200:
     gmSoup = BeautifulSoup(gmNews.text, "html.parser")
div_arts = gmSoup.find("div", attrs={"class": "news"})

links = []

links.append(div_arts.find("a").get("href"))

for i in div_arts.find_next_siblings():
    a = i.find("a")
    try:
        links.append(a.get("href"))
    except Exception as o:
        print(o)

urls_list = ["https://gamewave.fr" + x for x in links]

for url in urls_list:
     print(url)

list_titre = []
list_soustitre = []
list_image = []
list_texte= []

for lien in urls_list:

     try:
          art = requests.get(lien)
          if art.status_code == 200:

               soup_art = BeautifulSoup(art.text, "html.parser")
               #Extraire le  titre:
               infos = soup_art.find("div", attrs ={"id": "informations-content"})
               titre = infos.find("h1").get_text()
               list_titre.append(titre)

               #Extraire l'introduction:
               soustitre = soup_art.find("div", attrs={"id": "introduction"}).get_text()
               list_soustitre.append(soustitre)

               #Extraire article text
               texte = soup_art.find("div", attrs={"class": "left"}).get_text()
               list_texte.append(texte) 
               #extraire l'image de l'artcile 
               image = soup_art.find("div" , attrs={"id": "image"}).get("style")
               url = image.split("'")
               list_image.append(url[1])

     except:
          pass



#for titre in list_titre:
#     print(titre)
#    print('\n')

#for soustitre in list_soustitre:
     #print(soustitre)
     #print('\n')

for texte in list_texte:
     print(texte)
     print('\n')

for image in list_image:
     print(image)
     print('\n')
