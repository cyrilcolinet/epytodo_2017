##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from app.api import *
from flask import *

class Controller(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)

    def index_action(self, api):
        return render_template("index.html", api=api)

class AuthController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.api = API(app, conn)

    def register_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.user_create(username, password)
        flash(result)
        return redirect(url_for('route_home'))

    def signin_action(self, request):
        username = request.form['username']
        password = request.form['password']
        result = self.api.login(username, password)
        print(result)
        return redirect(url_for('route_home', api=result))

    def signout_action(self, request):
        result = self.api.logout()
        print(result)
        return redirect(url_for('route_home', api=result))

class UserController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)


class TaskController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
