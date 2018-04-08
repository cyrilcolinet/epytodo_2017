# -*- coding: utf-8 -*-
##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

import os
import locale
from app.controllers import *
from app.connection import *
from flask import *
import pymysql as sql

# Configure flask module
app = Flask(__name__)
app.config.from_object('config')
locale.setlocale(locale.LC_TIME, "")

def get_application():
    return app

# Configure database
conn = ConnectionManager(app)

def get_connection():
    return conn.get_connection()

@app.template_filter('autoversion')
def autoversion_filter(filename):
  fullpath = os.path.join('app/', filename[1:])
  try:
      timestamp = str(os.path.getmtime(fullpath))
  except OSError:
      return filename
  newfilename = "{0}?v={1}".format(filename, timestamp)
  return newfilename
