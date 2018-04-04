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

    def exists(self, username):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(1) FROM %s WHERE username = '%s'" % (self.table, username))
            exists = cur.fetchone()[0]
            cur.close()
            return True if exists == 1 else False
        except (Exception) as error:
            print(error)
            return True
        return True

    def create(self, username, password):
        salt = self.app.config['PASSWORD_SALT']
        try:
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            digest = hash.hexdigest()
            cur = self.conn.cursor()
            cur.execute("INSERT INTO %s (username, password) VALUES ('%s', '%s')"
                % (self.table, username, digest))
            self.conn.commit()
        except (Exception) as error:
            print(error)

    def get_id(self, username):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT user_id FROM %s WHERE username = '%s'" % (self.table, username))
            id = cur.fetchone()[0]
            cur.close()
            return id
        except (Exception) as err:
            print(err)
            return -1
        return -1

    def check_password(self, username, password):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT password FROM %s WHERE username = '%s'" % (self.table, username))
            pwd = cur.fetchone()[0]
            cur.close()
            salt = self.app.config['PASSWORD_SALT']
            hash = hashlib.sha512()
            hash.update(salt.encode())
            hash.update(password.encode())
            digest = hash.hexdigest()
            return True if digest == pwd else False
        except (Exception) as err:
            print(err)
            return False
        return False

class Task(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.table = "task"
