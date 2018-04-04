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
        return render_template("index.html")

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
        result = self.api.user_login(username, password)
        flash(result)
        return redirect(url_for('route_home'))

    def signout_action(self, request):
        result = self.api.user_logout()
        flash(result)
        return redirect(url_for('route_home'))

class UserController(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)

    def view_user_info_action(self):
        return render_template("index.html")

    def view_user_all_task_action(self):
        return render_template("index.html")

    def view_user_special_task_action(self):
        return render_template("index.html")

    def update_task_action(self, request):
        return redirect(url_for('route_home'))

    def create_task_action(self, request):
        return redirect(url_for('route_home'))

    def delete_task_action(self, request):
        return redirect(url_for('route_home'))
