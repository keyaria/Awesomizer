import time, threading, models, json, csv, isbnlib
from threading import Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from multiprocessing import Process

app = Flask(__name__)
socketio = SocketIO(app)

def get_ISBN_from_barcode(barcode):
    with open('ISBNs.csv', 'rb') as csvfile:
        book_list = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in book_list:
            if row[0] == barcode:
                return str(isbnlib.get_isbnlike(str(row[2]))[0])


#This is whatis called when you go to the website (localhost:5000).
#Sends all the information from database so the website can be populated
@app.route('/')
def index():
    res = models.get_all_books()
    return render_template('index.html', data = (res))

@app.route('/most-awesomized')
def most_awesome():
    res = models.get_all_books()
    return render_template('most-awesomized.html', data = (res))

@app.route('/about')
def about():
    return render_template('about.html')

#This recieves the request from scanner.py. Searches to see how many times it has been
#Scanned in in the database. If it hasn't been scanned before, make a new entry in database
#If it has been scanned before, add one to that and update
@app.route('/send_barcode/<barcode>', methods=['POST'])
def get_barcode_from_scanner(barcode):
    ISBN = get_ISBN_from_barcode(barcode)
    print(ISBN, "ISBN")
    book_info = isbnlib.meta(ISBN)
    print(book_info)
    book_cover = isbnlib.cover(ISBN)

    times_scanned = models.search_ISBN_get_times_scanned(ISBN)

    if times_scanned == None:
        models.insert_books(str(book_info['Title']), str(book_info['Authors']), str(ISBN), str(book_cover['thumbnail']), 1)
        res = [str(book_info['Title']), str(book_info['Authors']), str(ISBN), str(book_cover['thumbnail']), 1]
        socketio.emit('barcode', {'data': res}, namespace="/awesome")
    else:
        models.update_times_scanned(times_scanned + 1, ISBN)
        res = models.get_info_from_ISBN(ISBN)
        socketio.emit('update_data', {'data': res}, namespace="/awesome")

    return render_template('index.html', data = [])

#Gets called whenever someone connects to web site, probably don't need
@socketio.on('connect', namespace='/awesome')
def local_client_connect():
    print("connected")


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, host='0.0.0.0')
