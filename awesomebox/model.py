"""Insta485 model (database) API."""
import sqlite3
import flask
import awesomebox

def dict_factory(cursor, row):
    """
    Convert database row objects to a dictionary.

    This is useful for building dictionaries which are then
    used to render a template.  Note that
    this would be inefficient for large queries.
    """
    output = {}
    for idx, col in enumerate(cursor.description):
        output[col[0]] = row[idx]
    return output


def get_db():
    """Open a new database connection."""
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = sqlite3.connect(
            awesomebox.app.config['DATABASE_FILENAME'])
        flask.g.sqlite_db.row_factory = dict_factory

        # Foreign keys have to be enabled per-connection.  This is an sqlite3
        # backwards compatibility thing.
        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.sqlite_db


@awesomebox.app.teardown_appcontext
def close_db(error):
    # pylint: disable=unused-argument
    """Close the database at the end of a request."""
    if hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db.commit()
        flask.g.sqlite_db.close()

#Adds entry to database
def insert_books(title, author_name, ISBN, thumbnail, times_scanned):
    con = get_db()
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO books (title, author_name, ISBN, thumbnail, times_scanned) VALUES (?,?,?,?,?)", (title, author_name, ISBN, thumbnail, times_scanned))
    con.commit()

#Returns all entries in database
def get_all_books():
    con = get_db()
    cur = con.cursor()
    result = cur.execute("select * from books").fetchall()
    return (result)

#Updates the number of times a book as been scanned
def update_times_scanned(times_scanned, ISBN):
    con = get_db()
    cur = con.cursor()
    cur.execute("UPDATE books SET times_scanned = (?) WHERE ISBN = (?)", (times_scanned, ISBN))
    con.commit()

#Returns number of times a book has been scanned, None if 0
def search_ISBN_get_times_scanned(ISBN):
    con = get_db()
    cur = con.cursor()
    res = cur.execute("select * from books WHERE ISBN = (?)", [ISBN]).fetchall()
    if len(res) == 0:
        return None
    else:
        print(res)
        return int(res[0]["times_scanned"]) #returns times_scanned

#Returns all the info for one specific book
def get_info_from_ISBN(ISBN):
    con = get_db()
    cur = con.cursor()
    res = cur.execute("select * from books WHERE ISBN = (?)", [ISBN]).fetchall()
    return res