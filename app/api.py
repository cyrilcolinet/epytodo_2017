# -*- coding: utf-8 -*-
##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## api controller
##

from app import *
from app.models import *
from flask import *
import datetime

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
                    ret['error'] = "internal error"
                else:
                    self.user.create(username, password)
                    ret['result'] = "account created"
        return json.dumps(ret)

    def user_login(self, username, password):
        ret = {}
        if not username and not password:
            ret['error'] = "login or password does not match"
        else:
            if not self.user.exists(username):
                ret['error'] = "login or password does not match"
            elif not self.user.check_password(username, password):
                ret['error'] = "login or password does not match"
            else:
                session['username'] = username
                session['id'] = self.user.get_id(username)
                ret['result'] = "signin successful"
        return json.dumps(ret)

    def user_logout(self):
        ret = {}
        session.pop('username', None)
        session.pop('id', None)
        ret['result'] = "signout successful"
        return json.dumps(ret)

    def task_update(self, id, title, status, begin, end):
        ret = {}
        if session['username']:
            if self.task.id_exist(id):
                self.task.update_task(id, title, status, begin, end)
                ret['result'] = "update done"
            else:
                ret['error'] = "task id does not exist"
        else:
            ret['error'] = "you must be logged in"
        return json.dumps(ret)

    def task_create(self, title, begin, end, status):
        ret = {}
        if session['username']:
            if (title):
                if self.task.create_task(session['id'], title, begin, end, status):
                    ret['result'] = "new task added"
                else:
                    ret['error'] = "internal error"
            else:
                ret['error'] = "internal error"
        else:
            ret['error'] = "you must be logged in"
        return json.dumps(ret)

    def task_delete(self, id):
        ret = {}
        if session['username']:
            if self.task.id_exist(id):
                if self.task.delete_task(id):
                    ret['result'] = "deleted"
                else:
                    ret['error'] = 'internal error'
            else:
                ret['error'] = "task id does not exist"
        else:
            ret['error'] = "you must be logged in"
        return json.dumps(ret)

    def task_get_by_id(self, task_id):
        ret = {}
        if self.task.id_exist(task_id):
            res = self.task.get_task_by_id(task_id)
            if res == None:
                ret['error'] = "internal error"
            else:
                ret['result'] = res
        else:
            ret['error'] = "internal error"
        return json.dumps(ret)

    def task_get_all(self, user_id):
        ret = {}
        if self.user.exists_id(user_id):
            result = self.task.get_tasks_by_user_id(user_id)
            for i in range(0, len(result)):
                if result[i][2] != None:
                    time = datetime.datetime.strftime(result[i][2], "%A %d %b %Y, à %H:%S")
                    result[i][2] = time
                if result[i][3] != None:
                    time = datetime.datetime.strftime(result[i][3], "%A %d %b %Y, à %H:%S")
                    result[i][3] = time
            ret['result'] = result
        else:
            ret['error'] = "user doesn't exists"
        return json.dumps(ret)
