import sqlite3




def create_tables():
    con = sqlite3.connect("./database.sqlite")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS"players" (
	"id"	INTEGER,
	"name"	TEXT)""")
    
    con.commit()

def create_account(id, name):
    print("trying")
    """creates player 'account' """
    con = sqlite3.connect("./database.sqlite")
    cur = con.cursor()
    try:
        cur.execute("""SELECT id from players where id=?""", (id,))
        player = cur.fetchone()
        print(player)
        if player == None:
            cur.execute("""INSERT INTO players (id, name) VALUES (?,?)""", (id, name))
        
        con.commit()
        con.close()
        return "Stat placeholder"
    except Exception as e:
        print(e)



