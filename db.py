import sqlite3
DB_NAME = "messages.db"

def query(sql: str = "", data: tuple = ()):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit() 
        return cur.fetchall()  
    
def init_db():
    query('''CREATE TABLE IF NOT EXISTS messages (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 message TEXT NOT NULL
             )''')