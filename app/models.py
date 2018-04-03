##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from app import *
import hashlib

class User(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.table = "user"

    def user_exists(self, username):
        cur = self.conn.cursor()
        exists = 1
        cur.execute("SELECT COUNT(1) FROM %s WHERE username = '%s'" % (self.table, username))
        exists = cur.fetchone()[0]
        cur.close()
        return exists

    def user_create(self, username, password):
        salt = self.app.config['PASSWORD_SALT']
        hash = hashlib.sha512(b"")
        hash.update(b"" + salt)
        hash.update(b"" + password)
        digest = hash.hexdigest()
        print(digest)
