from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from ..database.db import db
from ..models.user import User
from werkzeug import exceptions


auth = Blueprint("auth", __name__)

@auth.route('/auth/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = User.query.filter_by(username=username).first()
        if user == None:
            return jsonify({"msg": "Bad username or password"}), 401
      
        access_token = create_access_token(identity=username)
        if user.password != password:
             raise exceptions.BadRequest("Wrong password!")
             
        return jsonify(access_token=access_token), 200


@auth.route('/auth/register', methods=['POST'])
def register():
    if request.method == "POST":
        try:
            req = request.get_json()
            username = req['username']
            email = req['email']
            password = req['password']
            new_user = User(username=username, email=email, password=password)

            existing_user = User.query.filter_by(username=username).first()
            print(existing_user)

            if existing_user:
                raise Exception
                

            db.session.add(new_user)
            db.session.commit()
            return jsonify("New user was added!"), 201
        except:
            return f"Username: {username} already exists! Please, choose another username and try again!"

