##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.config.from_object('config')

connection = pymysql.connect(host = "127.0.0.1", user = "root", password = "")
