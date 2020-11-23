import sqlite3

def conn(db_file):
    """Create a database conn to SQLite database"""

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e)

    dbCursor = conn.cursor()
    sql_query= """
    CREATE TABLE articles (
        id INTEGER PRIMARY KEY,
        titre TEXT,
        soustitre TEXT,
        img TEXT,
        author TEXT,
        lien TEXT,
        text TEXT
    )
    """
    dbCursor.execute(sql_query)

    conn.close()
    

if __name__ == '__main__':
    conn('arts.db')
