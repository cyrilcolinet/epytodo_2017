##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## vienws file
##

from app import app

## Index page
@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])

def route_home():
	return "Hello world !\n"

## User pages
@app.route('/user/<username>', methods = ['POST'])

def route_add_user(username):
	return "User added !\n"
