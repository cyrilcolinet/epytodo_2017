##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## __init__ file
##

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
