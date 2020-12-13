"""
Functions d'insertion et recherche des articles dans la base de données
"""
import sqlite3

def insertQuery(titre, stitre, lien, text, img="None", author="None"):
    """fonction qui se connecte à la base de données et insert les informations des articles 
        scrappées
        @param titre: titre de l'article 
        @param stitre: soustitre de l'article 
        @param lien: lien de l'article 
        @param text: text de l'article 
        @param img: img de l'article 
        @param author: auteur de l'article 
    """

    conn = None

    #Creation de la connexion à la base de données
    try:
        conn = sqlite3.connect('bd/arts.db')
    except Exception as e:
        print(e)

    #Creation du Cursor qui va gerer les requêtes
    dbCursor = conn.cursor()
    
    #Creation de la variable qui contient la requête d'insertion SQL
    sql_query= """
    INSERT INTO articles (
        titre,
        soustitre,
        img,
        author,
        lien,
        text
    ) VALUES (
        :titre,
        :stitre,
        :img,
        :author,
        :lien,
        :text
    )
    """
    #Execution de la requête avec le dictionaire des parametres passées à la fonction
    dbCursor.execute(sql_query, {
      'titre': titre,  
      'stitre': stitre,  
      'img': img,  
      'author': author,  
      'lien': lien,  
      'text': text,  
    })
    #Impression en console pour verfier que l'operation est reussi
    print("Ajout reussi")

    #Commit dans la base de données pour enregistrer les changements
    conn.commit()

    #Fermeture de la connexion
    dbCursor.close()

def rechercheQuery(critere):
    """
    Fonction qui recupere et retourne un article de la base de données sur un critere donné en parametre

    @param critere: Critere de recherche
    """

    #Creation de la connexion à la base de données
    conn = sqlite3.connect('bd/arts.db')
    #Creation d'une tuple avec les identifiants de chaque colonne
    conn.row_factory = sqlite3.Row

    #Creation du Cursor qui va gerer les requêtes
    dbCursor = conn.cursor()

    #Creation de la variable qui contient la requête de recherche SQL
    recherche = """
    select * from articles 
    where text like ?
    """

    #Execution de la requête avec le critere passée à la fonction
    dbCursor.execute(recherche, (f"%{critere}%",))
    #Recuperation du resultat
    resultat = dbCursor.fetchone()

    #Impression en console pour verification
    #print(resultat)

    #Fermeture de la connexion
    dbCursor.close()

    #Envoie du resultat
    return resultat

def verificationTitre():
    """
    Function qui recupere les titre des articles dans la base de données
    """

    #Creation de la connexion à la base de données
    conn = sqlite3.connect('bd/arts.db')

    #Creation du Cursor qui va gerer les requêtes
    dbCursor = conn.cursor()

    #Creation de la variable qui contient la requête de recherche SQL
    recherche = """
    select titre from articles 
    """

    #Execution de la requête avec le critere passée à la fonction
    dbCursor.execute(recherche)

    #Recuperation des resultats
    resultats = dbCursor.fetchall()

    #Création de liste vide pour enregistrer les titres 
    titresInBD = []

    #Deballage des tuples contenant les titres dans la liste créée
    for resultat in resultats:
        titresInBD.append(resultat[0])

    #Fermeture de la connexion
    dbCursor.close()

    #Envoie des resultats
    return titresInBD

def rechercheQueryADeuxCri(critere1, critere2):
    """
    Fonction qui recupere et retourne un article de la base de données sur deux criteres passées en parametre

    @param critere1: Premier critere de recherche
    @param critere2: Deuxieme critere de recherche
    """

    #Creation de la connexion à la base de données
    conn = sqlite3.connect('bd/arts.db')
    
    #Creation d'une tuple avec les identifiants de chaque colonne
    conn.row_factory = sqlite3.Row

    #Creation du Cursor qui va gerer les requêtes
    dbCursor = conn.cursor()

    #Creation de la variable qui contient la requête de recherche SQL
    recherche = """
    select * from articles 
    where text like :critere1 AND text like :critere2
    """

    #Execution de la requête avec les critere passées à la fonction
    dbCursor.execute(recherche, {
        'critere1': f"%{critere1}%",
        'critere2': f"%{critere2}%"
    })
    
    #Recuperation du resultat
    resultat = dbCursor.fetchone()

    #Impression en console pour verification
    #print(resultat)

    #Fermeture de la connexion
    dbCursor.close()

    #Envoie du resultat
    return resultat
