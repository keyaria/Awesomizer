"""
Awesomebox index (main) view.

URLs include:
/
"""
import os
import flask
import arrow
import awesomebox

@awesomebox.app.route('/', methods=['POST', 'GET'])
def show_index():
    return flask.render_template('index.html')

@awesomebox.app.route('/about/', methods=['GET'])
def show_about():
    return flask.render_template('about.html')