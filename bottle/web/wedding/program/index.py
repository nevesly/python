# -*- coding:utf-8 -*-

from bottle import Bottle, run, template, TEMPLATE_PATH
from bottle import get, post, request
from bottle import static_file
from bottle import error

DEBUG = True

app = Bottle()
TEMPLATE_PATH.insert(0,'/cygdrive/e/code/git/python/bottle/web/wedding/template')

@app.route("/")
def index():
    return template("index.html", name = "fuck")

run(app, host='localhost', port=8080, debug=DEBUG)
