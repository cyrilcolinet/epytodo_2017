##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## vienws file
##

from app import *

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])

def route_home():
    return Controller(app).index_action()

@app.route('/register', methods = ['POST'])
def route_register():

@app.route('/sigin', methods = ['POST'])
def route_sigin():

@app.route('/sigout', methods = ['POST'])
def route_sigout():

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
