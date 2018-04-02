##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from flask import Flask, render_template, request
import pymysql as sql
import sys

app = Flask(__name__)
app.config.from_object('config')

con = None

try:
	if app.config['DATABASE_SOCK'] == None:
		con = sql.connect(host=app.config['DATABASE_HOST'],
		                  user=app.config['DATABASE_USER'],
						  password=app.config['DATABASE_PASS'],
						  db=app.config['DATABASE_NAME'])
	else:
		con = sql.connect(unix=app.config['DATABASE_SOCK'],
		                  user=app.config['DATABASE_USER'],
						  password=app.config['DATABASE_PASS'],
						  db=app.config['DATABASE_NAME'])
except:
	print("Error during connection.")
	exit(84)
