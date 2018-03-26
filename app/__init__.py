##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from flask import Flask, render_template, request
import pymysql as sql
import Config

app = Flask(__name__)
app.config.from_object('Config')

connection = sql.connect(host=DATABASE_HOST, user=DATABASE_USER, password=DATABASE_PASS)
