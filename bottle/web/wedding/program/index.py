# -*- coding:utf-8 -*-

from bottle import Bottle, run, template, TEMPLATE_PATH
from bottle import get, post, request
from bottle import static_file
from bottle import error

DEBUG = True

import os
PROG_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(PROG_DIR)
TEMPLATE_PATH.insert(0, os.path.join(PROJ_DIR, 'template'))
STATIC = os.path.join(PROJ_DIR, 'static')

# app start
app = Bottle()

@app.route("/")
def index():
    return template("index.html", name = "fuck")

# Static files
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC)

run(app, host='0.0.0.0', port=8080, debug=DEBUG)
