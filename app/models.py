##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from app import *

class User(object):

    __tablename__ = "user"

    def __init__(self, app):
        self.app = app
        self.conn = get_connection()

    def user_exists(self, username):
        cur = self.conn.cursor
        cur.execute("SELECT COUNT(1) FROM %s WHERE username = %s" % (__tablename__, username))
        print(cur.description)
        print()
        for row in cur:
            print(row)
        cur.close()
