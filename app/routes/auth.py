from flask import Blueprint, request, jsonify
# from flask_login import logout_user
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..database.db import db
from ..models.user import User
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route('/auth/login', methods=['POST'])
def login():
    if request.method == "POST":
        try:
            username = request.json.get('username', None)
            password = request.json.get('password', None)
      
            user = User.query.filter_by(username=username).first()
           
            if user is None:
                return jsonify({"msg": "Bad username or password"}), 401
       
        
            authed = check_password_hash(user.password_hash, password) 
            print("USER", authed)
            if not authed:
                # return exceptions.Unauthorized('Incorrect password.')
                return "You've entered an incorrect password"

         
            access_token = create_access_token(identity=username)
           
            token = {
                 'success': True,
                 'token': access_token
            }
            if access_token:
                return jsonify(access_token=token), 200
           
        except:
            # raise exceptions.InternalServerError()
            return "server error", 505
    

# @auth.route("/auth/logout", method=['POST'])
# def logout():
#     if request.method == 'POST':
#         return jsonify("User has been successfully logged out!"), 201

@auth.route('/auth/register', methods=['POST'])
def register():
    if request.method == "POST":
        try:
            req = request.get_json()
            username = req['username']
            email = req['email']
            password = req['password']

            user = User.query.filter_by(username=username).first()

            if user:
                return jsonify("Username already exists!"), 202

            hashed_password = generate_password_hash(password)

            new_user = User(username=username, email=email, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
         
            return jsonify("New user was added!"), 201
            

        except:
            raise exceptions.InternalServerError()


@auth.route('/auth/users')
def get_all_users():
    users = User.query.all()
    all_users = jsonify([u.single_user() for u in users])
    return all_users
