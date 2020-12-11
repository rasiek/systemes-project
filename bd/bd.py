"""
Code de création de la base de données (à utiliser une seule fois)
"""

import sqlite3

def conn(db_file):
    """Create a database conn to SQLite database"""

    conn = None

    #Creation de la connexion à la base de données, etant donné que le fichier n'existait pas avant, 
    #la fonction connect du module sqlite3 créée un nouveau fichier.
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e)

    #Fermeture de la connexion
    conn.close()
    

if __name__ == '__main__':
    #Appel de la fonction au moment que le fichier python est ouvert
    conn('bd/arts.db')
