from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
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
                 'token': access_token,
                 'username': user.username,
                 'user_id': user.user_id
            }
            if access_token:
                return jsonify(access_token=token), 200
           
        except:
            # raise exceptions.InternalServerError()
            return "server error", 505
    



@auth.route('/auth/register/', methods=['POST'])
def register():
    if request.method == "POST":
        try:
            req = request.get_json()
            username = req['username']
            email = req['email']
            password = req['password']
            user = User.query.filter_by(username=username).first()
            print(user)
            hashed_password = generate_password_hash(password)
            
            print(hashed_password)
            if user:
                return jsonify("Username already exists!"), 202

            new_user = User(username=username, email=email, password_hash=hashed_password)

            db.session.add(new_user)
            db.session.commit()
         
            return jsonify("New user was added!"), 201
            

        except:
            raise exceptions.InternalServerError()

@auth.route('/auth/logout')
def logout():
    pass #! need to write logout route


@auth.route('/auth/users')
def get_all_users():
    users = User.query.all()
    all_users = jsonify([u.single_user() for u in users])
    return all_users


