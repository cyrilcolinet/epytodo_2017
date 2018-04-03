##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## connection file
##

from app import *
import pymysql as sql

class ConnectionManager(object):

    cononection = None

    def __init__(self, app):
        self.app = app

    def connect(self):
        try:
            if app.config['DATABASE_SOCK'] == None:
                connection = sql.connect(host=app.config['DATABASE_HOST'],
                                         user=app.config['DATABASE_USER'],
                                         password=app.config['DATABASE_PASS'],
                                         db=app.config['DATABASE_NAME'])
            else:
                connection = sql.connect(unix=app.config['DATABASE_SOCK'],
                                         user=app.config['DATABASE_USER'],
                                         password=app.config['DATABASE_PASS'],
                                         db=app.config['DATABASE_NAME'])
            if connection == None:
                raise Exception
        except (Exception) as error:
            print(error)
            exit(84)

    def get_connection(self):
        return connection
