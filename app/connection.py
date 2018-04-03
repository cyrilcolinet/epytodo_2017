##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## connection file
##

from app import *
import pymysql as sql

class ConnectionManager(object):

    def __init__(self, app):
        self.app = app
        self.conn = None
        self.connect(app.config)

    def connect(self, config):
        try:
            if config['DATABASE_SOCK'] == None:
                self.conn = sql.connect(host=config['DATABASE_HOST'],
                                         user=config['DATABASE_USER'],
                                         password=config['DATABASE_PASS'],
                                         db=config['DATABASE_NAME'])
            else:
                self.conn = sql.connect(unix=config['DATABASE_SOCK'],
                                         user=config['DATABASE_USER'],
                                         password=config['DATABASE_PASS'],
                                         db=config['DATABASE_NAME'])
            if self.conn == None:
                raise Exception
        except (Exception) as error:
            print(error)
            exit(84)

    def get_connection(self):
        return self.conn
