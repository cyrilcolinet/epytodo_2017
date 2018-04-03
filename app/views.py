##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## views file
##

from app import *

@app.route('/', methods = ['GET'])
def route_home():
    controller = Controller(app, get_connection())
    return controller.index_action()

@app.route('/register', methods = ['POST'])
def route_register():
    controller = AuthController(app, get_connection())
    return controller.register_action(request)

@app.route('/sigin', methods = ['POST'])
def route_sigin():
    return

@app.route('/sigout', methods = ['POST'])
def route_sigout():
    return

@app.route('/user', methods = ['GET'])
def route_user_info():
    return

@app.route('/user/task', methods = ['GET'])
def route_user_all_task():
    return

@app.route('/user/task/id', methods = ['GET'])
def route_user_special_task():
    return

@app.route('/user/task/id', methods = ['POST'])
def route_update_task():
    return

@app.route('/user/task/add', methods = ['POST'])
def route_create_task():
    return

@app.route('/user/task/del/id', methods = ['POST'])
def route_delete_task():
    return
