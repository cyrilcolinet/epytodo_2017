##
## EPITECH PROJECT, 2018
## epytodo_2017
## File description:
## views file
##

from app import *

## Index routes
@app.route('/', methods = ['GET'])
def route_home():
    controller = Controller(app, get_connection())
    return controller.index_action()

## Auth system
@app.route('/register', methods = ['POST'])
def route_register():
    controller = AuthController(app, get_connection())
    return controller.register_action(request)

@app.route('/signin', methods = ['POST'])
def route_signin():
    controller = AuthController(app, get_connection())
    return controller.signin_action(request)

@app.route('/signout', methods = ['POST'])
def route_signout():
    controller = AuthController(app, get_connection())
    return controller.signout_action(request)

## User routes
@app.route('/user', methods = ['GET'])
def route_user_info():
    controller = UserController(app, get_connection())
    return controller.view_user_info_action()

@app.route('/user/task', methods = ['GET'])
def route_user_all_task():
    controller = UserController(app, get_connection())
    return controller.view_user_all_task_action()

@app.route('/user/task/id', methods = ['GET'])
def route_user_special_task(id):
    controller = UserController(app, get_connection())
    return controller.view_user_special_task_action(id)

@app.route('/user/task/id', methods = ['POST'])
def route_update_task(id):
    controller = UserController(app, get_connection())
    return controller.update_task_action(request, id)

@app.route('/user/task/add', methods = ['POST'])
def route_create_task():
    controller = UserController(app, get_connection())
    return controller.create_task_action(request)

@app.route('/user/task/del/id', methods = ['POST'])
def route_delete_task(id):
    controller = UserController(app, get_connection())
    return controller.delete_task_action(request, id)
