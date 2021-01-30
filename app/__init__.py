"""
Fichier d'initialisation 
"""

#Importation de la classe Flask de la librairie flask

from app.scrappers.gamewave import gamewaveScrapper
from app.scrappers.gamespot import gamespotScrapper
from flask import Flask

#Creation de la variable app qui va contenir le serveur
app = Flask(__name__)

#Importation des routes de l'application (s'est fait après la creation de la variable app pour eviter les redundances)
from app import routes

#Appel aux scrappers quand on initialise le serveur pour alimenter la base de données
# gamespotScrapper()
# gamewaveScrapper()

