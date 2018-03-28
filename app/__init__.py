##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from flask import Flask, render_template, request
import pymysql as sql

app = Flask(__name__)
app.config.from_object('config')

host = app.config['DATABASE_HOST']
user = app.config['DATABASE_USER']
passwd = app.config['DATABASE_PASS']
name = app.config['DATABASE_NAME']
unix = app.config['DATABASE_SOCK']

if unix == None:
	connection = sql.connect(host=host, user=user, password=passwd, db=name)
else:
	connection = sql.connect(unix_socket=unix, user=user, password=passwd, db=name)
