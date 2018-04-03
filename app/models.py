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
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(1) FROM %s WHERE username = '%s'" % (self.table, username))
            exists = cur.fetchone()[0]
            cur.close()
            return exists
        except (Exception) as error:
            print(error)
            exit(84)
        return

    def user_create(self, username, password):
        salt = self.app.config['PASSWORD_SALT']
        try:
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            digest = hash.hexdigest()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO %s (username, password) VALUES ('%s', '%s')"
                % (self.table, username, digest))
        except (Exception) as error:
            print(error)
            exit(84)
        return
