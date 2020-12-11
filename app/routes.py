"""
Routes de l'application
"""
#Importation des functions et modules pour le functionements des routes
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
        critere = request.form['recherche-form']


        try:

            critere2 = request.form['recherche-form2']

            art2Cri = rechercheQueryADeuxCri(critere, critere2)

            if art2Cri is None:

                noMatch = True
                return render_template("index.html", noMatch=noMatch)


            replaceList = [
                (critere, f"<U><strong class='critere'>{critere}</strong></U>"),
                (critere2, f"<U><strong class='critere'>{critere}</strong></U>")
            ]

            artText2Cri = art2Cri['text']

            for critere, critereStig in replaceList:
                
                artText2Cri = re.sub(critere, critereStig, art2Cri['text'], flags=re.I)

            context = {
            'titre': art2Cri['titre'],
            'soustitre': art2Cri['soustitre'],
            'author': art2Cri['author'],
            'text': artText2Cri,
            'lien': art2Cri['lien']
            }

            return render_template("index.html", **context)

        except Exception as e:
            print(e)            


        #Appel à la function rechercheQuery et recuperation des informations par rapport au critère
        art = rechercheQuery(critere)

        #Stimagtisation du critere de recherche dans le texte de l'article, en cherchant le critere à travers du module re
        #Utilisation du flag re.I pour chercher le critere en Majuscule et Miniscule
        art_text = re.sub(critere, f"<U><strong class='critere'>{critere}</strong></U>", art['text'], flags=re.I)
        
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

