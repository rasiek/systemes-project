"""
Recuperation des articles du site internet 'gamespot' en utilisant la librairie BeautifulSoup
"""

#Importation des librairies et modules neccesaires
from .. import functions as fc
import requests
from bs4 import BeautifulSoup


def gamespotScrapper():
    """
    Fonction qui cerche, recupère et enregistre des articles depuis le site internet gamespost.com 
    """
    #Creation du variable contenant le lien du site internet visé
    url = "https://www.gamespot.com/news/"

    #Requête 'GET' pour recuperer le site internet
    try:
        gsNews = requests.get(url)
    except Exception as e:
        print("Error:")
        print(e)
        print("\n")
        
    #Condition pour valider la requête et recuperation des informations sans les balises HTML avec un parser 'lxml'
    #Transformation du contenu en objet BeautifulSoup 
    if gsNews.status_code == 200:
        gsSoup = BeautifulSoup(gsNews.text, "lxml")

    #Utilisation des methodes find de la librairie bs pour chercher et recuperer les liens articles dans le site internet 
    div_arts = gsSoup.find("div", attrs={"class": "horizontal-card-item"})

    #Création de la liste qui va contenir les liens
    as_links = []

    #Ajout des liens à la liste
    as_links.append(div_arts.find("a", "horizontal-card-item__link").get("href"))

    #Ajout des liens à la liste
    for i in div_arts.find_next_siblings():
        a = i.find("a", "horizontal-card-item__link")
        try:
            as_links.append(a.get("href"))
        except Exception as e:
            print(e)


    urls_list = ["https://www.gamespot.com" + x for x in as_links]

    #Boucle for pour transformer le contenu de chaque article en objet BeautifulSoup et l'ajouter dans la base de données
    for url in urls_list:
        try:
            art = requests.get(url)
            if art.status_code == 200:
                soup_art = BeautifulSoup(art.text, "lxml")

                #Appel à la fonction verificationTitre pour creer une liste avec les titres des articles déjà enrregistrès dans la base de données
                liste_verification = fc.verificationTitre()

                #Extraction du titre
                title = soup_art.find("h1", attrs={"class": "news-title"}).get_text()

                #Conditionnel pour verifier si le titre extrait de l'article existe déjà dans la base de données 
                if title in liste_verification:
                    #print('article déjà enregistré')
                    pass

                else:

                    #Extraction du soustitre
                    subTitle = soup_art.find("h2", attrs={"class": "news-deck"}).get_text()

                    #Extraction de l'auteur
                    author = soup_art.find("a", "byline-author__name").get_text()

                    #Extraction du text de l'article
                    art_text = soup_art.find("div", attrs={"class": "js-content-entity-body"}).find_all("p")
                    textString = ""
                    for e in art_text:
                        textString += e.get_text() + "\n"

                    #Appel à la fonction insertQuery pour inserer l'article dans la base de données
                    fc.insertQuery(title, subTitle, url, textString, author)

        except:
            pass


