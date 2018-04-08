# -*- coding: utf-8 -*-
##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## models
##

from app import *
from flask import *
import hashlib
import time
from datetime import datetime

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
            cur.execute("SELECT COUNT(1) FROM %s WHERE username = '%s'"
                % (self.table, username))
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
            cur.execute("SELECT COUNT(1) FROM %s WHERE user_id = '%s'"
                % (self.table, user_id))
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
            cur.execute("SELECT user_id FROM %s WHERE username = '%s'"
                % (self.table, username))
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
            cur.execute("SELECT password FROM %s WHERE username = '%s'"
                % (self.table, username))
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

    def id_exist(self, id):
        try:
            cur = self.conn.cursor(id)
            cur.execute("SELECT COUNT(1) FROM %s WHERE task_id = '%d'"
                % (self.table, id))
            exists = cur.fetchone()[0]
            cur.close()
            return True if exists == 1 else False
        except (Exception) as err:
            print(err)
        return True

    def get_task_by_id(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM %s WHERE task_id = '%d'"
                % (self.table, id))
            task = list(cur.fetchall()[0])
            cur.close()
            return task
        except (Exception) as err:
            print(err)
        return None

    def get_tasks_by_user_id(self, user_id):
        tasks = []
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT fk_task_id FROM %s WHERE fk_user_id = '%d'"
                % (self.fk, user_id))
            ids = list(cur.fetchall())
            cur.close()
            for id in ids:
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM %s WHERE task_id = '%d'"
                    % (self.table, id[0]))
                task = list(cur.fetchall()[0])
                tasks.append(task)
                cur.close()
            return tasks
        except (Exception) as err:
            print(err)
        return tasks

    def update_task(self, task_id, title, status, begin, end):
        try:
            cur = self.conn.cursor()
            if not "None" in end and not end == None:
                print(end)
                format = '%Y-%m-%dT%H:%M:%S'
                new_format = '%Y-%m-%d %H:%M:%S'
                datetime.strptime(end, format).strftime(new_format)
                print(end)
                cur.execute("UPDATE %s SET 'begin' = %d WHERE task_id = '%d'"
                    % (begin, self.table))
                cur.close()
                cur = self.conn.cursor()
            if not "None" in end and not end == None:
                print(end)
                format = '%Y-%m-%dT%H:%M:%S'
                new_format = '%Y-%m-%d %H:%M:%S'
                datetime.strptime(end, format).strftime(new_format)
                print(end)
                cur.execute("UPDATE %s SET 'end' = %d WHERE task_id = '%d'"
                    % (end, self.table))
                cur.close()
                cur = self.conn.cursor()
            if not "None" in name or not name == None:
                cur.execute("UPDATE %s SET 'title' = %s WHERE task_id = '%d'"
                    % (title, self.table))
                cur.close()
                cur = self.conn.cursor()
            if not "None" in status or not status == None:
                cur.execute("UPDATE %s SET 'status' = %s WHERE task_id = '%d'"
                    % (status, self.table))
            self.conn.commit()
            cur.close()
        except (Exception) as err:
            print(err)

    def create_task(self, user_id, title, begin, end, status):
        try:
            cur = self.conn.cursor()
            if not begin == "None" and not begin == None:
                print(begin)
                format = '%Y-%m-%dT%H:%M:%S'
                new_format = '%Y-%m-%d %H:%M:%S'
                datetime.strptime(begin, format).strftime(new_format)
                print(begin)
                cur.execute("INSERT INTO %s `begin` VALUES '%d'"
                    % (self.table, begin))
                cur.close()
                cur = self.conn.cursor()
            if not end == "None" and not end == None:
                print(end)
                format = '%Y-%m-%dT%H:%M:%S'
                new_format = '%Y-%m-%d %H:%M:%S'
                datetime.strptime(end, format).strftime(new_format)
                print(end)
                cur.execute("INSERT INTO %s `end` VALUES '%d'"
                    % (self.table, end))
                cur.close()
                cur = self.conn.cursor()
            cur.execute("INSERT INTO %s (`title`, `status`) VALUES ('%s', '%s')"
                % (self.table, title, status))
            self.conn.commit()
            id = cur.lastrowid
            cur.close()
            if not id:
                return False
            cur = self.conn.cursor()
            cur.execute("INSERT INTO %s (fk_user_id, fk_task_id) VALUES (%d, %d)"
                % (self.fk, user_id, id))
            self.conn.commit()
            cur.close()
        except (Exception) as err:
            print(err)
            return False
        return True

    def delete_task(self, id):
        id = int(id)
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(1) FROM %s WHERE fk_task_id = %d AND fk_user_id = %d"
                % (self.fk, id, session['id']))
            res = cur.fetchone()[0]
            cur.close()
            if res != 1:
                return False
            cur = self.conn.cursor()
            cur.execute("DELETE FROM %s WHERE fk_task_id = %d AND fk_user_id = %d"
                % (self.fk, id, session['id']))
            self.conn.commit()
            cur.close()
            cur = self.conn.cursor()
            cur.execute("DELETE FROM %s WHERE task_id = %d"
                % (self.table, id))
            self.conn.commit()
            cur.close()
        except (Exception) as err:
            print(err)
            return False
        return True
