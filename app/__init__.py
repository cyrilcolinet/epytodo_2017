##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from app.controllers import *
from app.connection import *
from flask import *
import pymysql as sql

# Configure flask module
app = Flask(__name__)
app.config.from_object('config')

def get_application():
    return app

# Configure database
conn = ConnectionManager(app)

def get_connection():
    return conn.get_connection()
