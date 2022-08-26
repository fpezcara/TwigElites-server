from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


main_routes = Blueprint("main", __name__)

@main_routes.route('/')
def welcome():
    return "Twigelites Server!"

@main_routes.route('/token', methods=['POST'])
def create_token():
    email = request.json.get('email', None)
    password = request.json.get('email', None)
    
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


