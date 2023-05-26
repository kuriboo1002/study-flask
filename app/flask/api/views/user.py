from flask import Blueprint, request, jsonify
from api.models.user import User, UserSchema, users_schema
import json

user = Blueprint('user', __name__, url_prefix='/users')


@user.route('/<int:id>', methods=['GET'])
def getUser(id):
    user = User.searchBy(id)
    output = UserSchema().dump(user)
    return jsonify(output), 200


@user.route('/', methods=['GET'])
def getUsers():
    users = User.searchAll()
    outputs = users_schema.dump(users)
    return jsonify(outputs), 200


@user.route('/', methods=['POST'])
def createUser():
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)

    user = User.create(userData)
    output = UserSchema().dump(user)
    return jsonify(output), 200


@user.route('/<int:id>', methods=['PUT'])
def updateUser(id):
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)

    if id != userData['id']:
        return jsonify("クエリパラメータとRequestBodyのidが一致しない"), 400

    user = User.update(id, userData)
    output = UserSchema().dump(user)
    return jsonify(output), 200


@user.route('/<int:id>', methods=['DELETE'])
def deleteUser(id):
    User.delete(id)
    return jsonify("OK"), 200
