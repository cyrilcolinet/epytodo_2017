##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## controllers file
##

from app import *
from app.models import *
from flask import render_template

user = User()

class Controller(object):

    def index_action(self):
        ##user.user_exists("cyril")
        return render_template("index.html")

class UserController(object):

    controller = None

    def __init__(self):
        self.controller = new Controller()
