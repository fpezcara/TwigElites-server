from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


auth = Blueprint("auth", __name__)

@auth.route('/auth/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    email = request.json.get('email', None)
    password = request.json.get('email', None)
    print(str(username))
    
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@auth.route('/auth/register', methods=['POST'])
def register():
    pass
