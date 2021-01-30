"""
Recuperation des articles du site internet 'gamewave' en utilisant la librairie BeautifulSoup
"""

import requests
from .. import functions as fc
from bs4 import BeautifulSoup


def gamewaveScrapper():

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

     for lien in urls_list:

          try:
               art = requests.get(lien)
               if art.status_code == 200:

                    soup_art = BeautifulSoup(art.text, "html.parser")
                    #Extraire le  titre:
                    infos = soup_art.find("div", attrs ={"id": "informations-content"})
                    titre = infos.find("h1").get_text()


                    #Appel à la fonction verificationTitre pour creer une liste avec les titres des articles déjà enrregistrès dans la base de données
                    liste_verification = fc.verificationTitre()

                    #Conditionnel pour verifier si le titre extrait de l'article existe déjà dans la base de données 
                    if titre in liste_verification:
                         #print('article déjà enregistré')
                         pass
                    else:
                         #Extraire l'introduction:
                         soustitre = soup_art.find("div", attrs={"id": "introduction"}).get_text()
                    
                         #Extraire article text
                         texte = soup_art.find("div", attrs={"class": "left"}).get_text()
                    
                         #extraire l'image de l'artcile 
                         image = soup_art.find("div" , attrs={"id": "image"}).get("style")
                         url_img = image.split("'")
                         
                         fc.insertQuery(titre, soustitre, lien, texte, "Gamewave", url_img[1])

          except:
               pass



