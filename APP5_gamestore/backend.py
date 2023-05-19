import sqlite3

def make_table():
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Table1(id INTEGER PRIMARY KEY, Title text, Year integer, Type text)")
    con.commit()
    con.close()

def add_it(title, year, Type):
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Table1 VALUES(NULL, ?, ?, ?)", (title, year, Type))
    con.commit()
    con.close()

def del_it(ID):
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Table1 WHERE id = ?", (ID,))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Table1")
    rows = cur.fetchall()
    con.close()
    return rows   

def upd(id, title, year, Type):
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("UPDATE Table1 SET title=?, year=?, type=? WHERE id=?", (title, year, Type, id))
    con.commit()
    con.close()

def search(title="", year="", Type=""):
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Table1 WHERE title=? OR year=? OR type=?",(title, year, Type))
    rows = cur.fetchall()
    con.close()
    return rows



make_table()


