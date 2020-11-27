import sqlite3

def insertQuery(titre, stitre, img, lien, text, author="Pas d'author"):
    """Create a database conn to SQLite database"""

    conn = None

    try:
        conn = sqlite3.connect('arts.db')
    except Exception as e:
        print(e)

    dbCursor = conn.cursor()

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
    try:
        dbCursor.execute(sql_query, {
        'titre': titre,  
        'stitre': stitre,  
        'img': img,  
        'author': author,  
        'lien': lien,  
        'text': text,  
        })
    except Exception as e:
        print(e)

    print("true")

    conn.close()


def rechercheQuery(critéres):

    try:

        conn = sqlite3.connect('arts.db')
    except Exception as e:
        print(e)

    dbCursor = conn.cursor()

    recherche = """
    select * from articles 
    where text like ?
    """
    dbCursor.execute(recherche, (f"%{critéres}",))
    resultat = dbCursor.fetchone()
    
    print(resultat)
    dbCursor.close()

    
