"""REST API for likes."""
import flask
import awesomebox
import isbnlib
import requests
import json
from awesomebox.api.error_handler import InvalidUsage

def get_ISBN_from_barcode(barcode):
    info = requests.get("https://mirlyn.lib.umich.edu/api/simple/v1/barcode/{}".format(barcode))
    print(info.text)

    return json.loads(info.text)['docs'][0]['isbn'][0]

@awesomebox.app.route('/api/v1/awesomize/<int:barcode>/', methods=["POST", "GET"])
def awesomize_book(barcode):
    ISBN = get_ISBN_from_barcode(barcode)
    book_info = isbnlib.meta(ISBN)
    book_cover = isbnlib.cover(ISBN)

    times_scanned = awesomebox.model.search_ISBN_get_times_scanned(ISBN)

    if times_scanned == None:
        awesomebox.model.insert_books(str(book_info['Title']), str(book_info['Authors']), str(ISBN), str(book_cover['thumbnail']), 1)
        res = {
            'title': str(book_info['Title']), 
            'authors': str(book_info['Authors']), 
            'ISBN': str(ISBN),
            'thumbnail': str(book_cover['thumbnail']),
            'times_scanned': 1
        }
    else:
        awesomebox.model.update_times_scanned(times_scanned + 1, ISBN)
        res = awesomebox.model.get_info_from_ISBN(ISBN)

    return flask.jsonify(res), 201