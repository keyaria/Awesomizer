import sqlite3 as sql

#Adds entry to database
def insert_books(title, author_name, ISBN, thumbnail, times_scanned):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO books (title, author_name, ISBN, thumbnail, times_scanned) VALUES (?,?,?,?,?)", (title, author_name, ISBN, thumbnail, times_scanned))
        con.commit()

#Returns all entries in database
def get_all_books():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("select * from books").fetchall()
        result = [list(map(str, eachTuple)) for eachTuple in result]
        print (result)
        return (result)

#Updates the number of times a book as been scanned
def update_times_scanned(times_scanned, ISBN):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE books SET times_scanned = (?) WHERE ISBN = (?)", (times_scanned, ISBN))
        con.commit()

#Returns number of times a book has been scanned, None if 0
def search_ISBN_get_times_scanned(ISBN):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        res = cur.execute("select * from books WHERE ISBN = (?)", [ISBN]).fetchall()
        if len(res) == 0:
            return None
        else:
            return int(res[0][4]) #returns times_scanned

#Returns all the info for one specific book
def get_info_from_ISBN(ISBN):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        res = cur.execute("select * from books WHERE ISBN = (?)", [ISBN]).fetchall()
        return res
