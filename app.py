# -*- coding: utf-8 -*-
from flask import Flask, request
from Model.User import User
from service.UserService import UserService

app = Flask(__name__)


@app.route("/v1/user", methods=['POST'])
def set_user():
    return UserService.save_user(User(**request.json))


@app.route("/v1/user", methods=['GET'])
def get_user():
    id = request.args.get("id")
    return UserService.get_user(id)


@app.route("/v1/user", methods=['PUT'])
def update_user():
    id = request.args.get("id")
    return UserService.update_user(id)


@app.route("/v1/user", methods=['DELETE'])
def del_user():
    id = request.args.get("id")
    return UserService.delete_user(id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
