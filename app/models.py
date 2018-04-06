##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from app import *
from flask import *
import hashlib

## User Model
class User(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.table = "user"
        self.fk = "user_has_task"

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

    def exists_id(self, user_id):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(1) FROM %s WHERE user_id = '%s'" % (self.table, user_id))
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
            cur.close()
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

## Task Model
class Task(object):

    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        self.table = "task"
        self.fk = "user_has_task"

    def get_tasks_by_user_id(self, user_id):
        tasks = []
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT fk_task_id FROM %s WHERE fk_user_id = %d" % (self.fk, user_id))
            ids = list(cur.fetchall())
            cur.close()
            for id in ids:
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM %s WHERE task_id = %d" % (self.table, id[0]))
                task = list(cur.fetchall()[0])
                tasks.append(task)
                cur.close()
            return tasks
        except (Exception) as err:
            print(err)
        return tasks

    def create_task(self, user_id, name):
        try:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO %s (id, title) VALUES ('%s', '%s')"
                % (self.table, user_id, name))
            self.conn.commit()
        except (Exception) as err:
            print(err)
