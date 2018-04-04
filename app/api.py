##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## api controller
##

from app import *
from app.models import *
from flask import *

class API(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.user = User(app, conn)
        self.task = Task(app, conn)

    def user_create(self, username, password):
        ret = {}
        if not username.isalnum():
            ret['error'] = "internal error"
        else:
            if self.user.exists(username):
                ret['error'] = "account already exists"
            else:
                if not username and not password:
                    self.user.create(username, password)
                    ret['error'] = "internal error"
                else:
                    self.user.create(username, password)
                    ret['result'] = "account created"
        return json.dumps(ret)
