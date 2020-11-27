import sqlite3

def insertQuery(titre, stitre, lien, text, img="None", author="None"):
    """Create a database conn to SQLite database"""

    conn = None

    try:
        conn = sqlite3.connect('/bd/arts.db')
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
    dbCursor.execute(sql_query, {
      'titre': titre,  
      'stitre': stitre,  
      'img': img,  
      'author': author,  
      'lien': lien,  
      'text': text,  
    })

    print("Ajout reussi")

    dbCursor.close()
