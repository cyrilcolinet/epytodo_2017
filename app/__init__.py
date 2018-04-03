##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

#from app.models import *
from flask import *
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')

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

# Configuration of models
#user = User("user")
