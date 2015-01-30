# -*- coding:utf-8 -*-

from bottle import Bottle, run, template
from bottle import get, post, request
from bottle import static_file
from bottle import error

DEBUG = True

# default application
app = Bottle()

@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/')
@app.route('/hello/<name>')
def greet(name = "Guest"):
    return template("Hello <strong>{{name}}</strong>, how do you do?", name = name)

# Login
@app.get('/login')
def login():
    return '''
        <form action="/login" method="post">
                User Name: <input name="username" type="text" />
                Password: <input name="password" type="password" />
                <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if not check_login(username, password):
        return "<p>Login failed.</p>"

    return "<p>Login information was correct.</p>"

# Static files
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/cygdrive/e/code/python/bottle/develop/web/static')

# handle error
@app.error(404)
def error404(error):
    return "<strong>Nothing here, sorry</strong>"

############################################
# util
############################################
def check_login(username, password):
    if username =="Seven" and password == "123456": 
        return True
    return False

run(app, host='0.0.0.0', port=8080, debug=DEBUG)
