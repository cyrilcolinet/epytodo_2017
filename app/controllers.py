##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from flask import render_template

class Controller(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)

    def index_action(self):
        self.user.user_exists("cyril")
        return render_template("index.html")

class UserController(object):

    def __init__(self, app):
        self.app = app

class TaskController(object):

    def __init__(self, app):
        self.app = app

class AuthController(object):

    def __init__(self, app):
        self.app = app
