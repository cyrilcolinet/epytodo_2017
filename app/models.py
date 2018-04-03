##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from app import *

class User(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.table = "user"

    def user_exists(self, username):
        cur = self.conn.cursor()
        exists = 1
        cur.execute("SELECT COUNT(1) FROM %s WHERE username = '%s'" % (self.table, username))
        exists = cur.fetchone()
        if exists == 1:
            print("User exists")
        else:
            print("User doesn't exists")
        cur.close()
