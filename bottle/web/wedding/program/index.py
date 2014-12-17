# -*- coding:utf-8 -*-

from bottle import Bottle, run, template, TEMPLATE_PATH
from bottle import get, post, request
from bottle import static_file
from bottle import error

DEBUG = True

app = Bottle()
TEMPLATE_PATH.insert(0,'/cygdrive/e/code/git/python/bottle/web/wedding/template')
STATIC='/cygdrive/e/code/git/python/bottle/web/wedding/static'

@app.route("/")
def index():
    return template("index.html", name = "fuck")

# Static files
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC)

run(app, host='0.0.0.0', port=8080, debug=DEBUG)
