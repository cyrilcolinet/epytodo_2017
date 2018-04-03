##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## vienws file
##

from app import *

## Index page
@app.route('/', methods = ['GET'])
def route_main():
    UserController().bite()
    return Controller().index_action()

##register
@app.route('/register', methods = ['POST'])
def route_register():

##sigin
@app.route('/sigin', methods = ['POST'])
def route_sigin():

##sigout
@app.route('/sigout', methods = ['POST'])
def route_sigout():

##user
@app.route('/user', methods = ['GET'])
def route_user_info():

@app.route('/user/task', methods = ['GET'])
def route_user_all_task():

@app.route('/user/task/id', methods = ['GET'])
def route_user_special_task():

@app.route('/user/task/id', methods = ['POST'])
def route_update_task():

@app.route('/user/task/add', methods = ['POST'])
def route_create_task():

@app.route('/user/task/del/id', methods = ['POST'])
def route_delete_task():
