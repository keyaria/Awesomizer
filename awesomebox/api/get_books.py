"""REST API for likes."""
import flask
import awesomebox
import ast
import operator
from awesomebox.api.error_handler import InvalidUsage


@awesomebox.app.route('/api/v1/books/', methods=["GET"])
def get_books():
    result = awesomebox.model.get_all_books()
    updated_result = []
    for res in result:
        authors = ast.literal_eval(res['author_name'])
        updated_authors = ""
        count = 0
        total = len(authors)
        for author in authors:
            if count > 0 and count < total:
                updated_authors = updated_authors + ", " + (str(author))
            else:
                updated_authors = updated_authors + " " + (str(author))
            count += 1
        res['author_name'] = updated_authors
        updated_result.append(res)

    if flask.request.args.get('sorted'):
        updated_result.sort(key=operator.itemgetter('times_scanned'), reverse=True)
        return flask.jsonify(updated_result)

    return flask.jsonify(updated_result)