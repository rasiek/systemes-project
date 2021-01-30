"""
Routes de l'application
"""
#Importation des functions et modules pour le fonctionements des routes
from app.scrappers.gamespot import gamespotScrapper
from app.functions import rechercheQuery, rechercheQueryADeuxCri
from flask import render_template, request
from app import app
import re



#Creation du decorator qui reçoi une methode post
@app.route('/', methods=['POST', 'GET'])
def recherche():
    #Condition qui valide l'existance d'une requête "POST" et recupère l'information contenu dans le bar de recherche d'ID "recherche-form"
    if request.method == 'POST':
        
        #Creation d'une variable qui contient le critere de recherche
        critere = request.form['input-critere1']

        #Validation de l'existance d'une deuxième critère de recherche
        if request.form['input-critere2'] == "":

            #Si l'input[''input-critere2] est un String vide, on sorte du conditionnel
            pass
        else:
            #Creation d'une autre variable qui contient le deuxième critère de recherche
            critere2 = request.form['input-critere2']

            #Appel à la function rechercheQueryADeuxCri et recuperation des informations par rapport au critère
            art2Cri = rechercheQueryADeuxCri(critere, critere2)

            if art2Cri is None:

                noMatch = True
                return render_template("index.html", noMatch=noMatch)

            #Stimagtisation des critères de recherche dans le texte de l'article, en cherchant les critères à travers du module re
            #Utilisation du flag re.I pour chercher les critères en Majuscule et Miniscule
            #Uilisation d'une liste pour enregistrer le critère à chercher dans le text et son remplacement
            replaceList = [
                (critere, f"<U><strong class='critere'>{critere.capitalize()}</strong></U>"),
                (critere2, f"<U><strong class='critere'>{critere2.capitalize()}</strong></U>")
            ]
            #Création de la variable qui contient le text de l'article
            artText2Cri = art2Cri['text']

            #Boucle for où il est appelé la methode sub pour remplacer les critères originaux pour le code qui va les stigmatiser
            for critere, critereStig in replaceList:
                artText2Cri = re.sub(critere, critereStig, artText2Cri, flags=re.I)
                print(critere, critereStig)

            #Creation du dictionaire contenant les informations de l'article trouvé
            context = {
            'titre': art2Cri['titre'],
            'soustitre': art2Cri['soustitre'],
            'author': art2Cri['author'],
            'text': artText2Cri,
            'lien': art2Cri['lien']
            }
            #Appel à la function render_template pour afficher le fichier html lié à la route et 
            #envoie du dictionaire avec l'article
            return render_template("index.html", **context)          

        #Si l'input[''input-critere2] est un String vide, on continue au dessus

        #Appel à la function rechercheQuery et recuperation des informations par rapport au critère
        art = rechercheQuery(critere)

        #Stimagtisation du critere de recherche dans le texte de l'article, en cherchant le critere à travers du module re
        #Utilisation du flag re.I pour chercher le critere en Majuscule et Miniscule
        art_text = re.sub(critere, f"<U><strong class='critere'>{critere.capitalize()}</strong></U>", art['text'], flags=re.I)
        
        #Creation du dictionaire contenant les informations de l'article trouvé  
        context = {
        'titre': art['titre'],
        'soustitre': art['soustitre'],
        'author': art['author'],
        'text': art_text,
        'lien': art['lien']
        }

        #Appel à la function render_template pour afficher le fichier html lié à la route et 
        #envoie du dictionaire avec l'article
        return render_template('index.html', **context)

    #S'il n'existe pas une requête 'POST', on retourne le fichier HTML
    return render_template('index.html')

