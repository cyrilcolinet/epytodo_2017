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

connection = sql.connect(host=app.config['DATABASE_HOST'],
						user=app.config['DATABASE_USER'],
						password=app.config['DATABASE_PASS'])
