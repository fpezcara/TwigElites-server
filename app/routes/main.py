from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


main_routes = Blueprint("main", __name__)

@main_routes.route('/')
def welcome():
    return "Twigelites Server!"

@main_routes.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('email', None)
    print(str(username))
    
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


