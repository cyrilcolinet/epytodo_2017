##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from app.controllers import *
from flask import Flask
import pymysql as sql

# Configure flask module
app = Flask(__name__)
app.config.from_object('config')

# Configure database
conn = None

try:
    if app.config['DATABASE_SOCK'] == None:
        conn = sql.connect(host=app.config['DATABASE_HOST'],
                           user=app.config['DATABASE_USER'],
                           password=app.config['DATABASE_PASS'],
                           db=app.config['DATABASE_NAME'])
    else:
        conn = sql.connect(unix=app.config['DATABASE_SOCK'],
                           user=app.config['DATABASE_USER'],
                           password=app.config['DATABASE_PASS'],
                           db=app.config['DATABASE_NAME'])
    if conn == None:
        raise Exception
except (Exception) as err:
    print(err)
    exit(84)
