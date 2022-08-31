from flask import Blueprint
# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required

from flask_mail import Message

from app.mailers import mail_config


main_routes = Blueprint("main", __name__)
mail_routes = Blueprint("mail", __name__)


mail = mail_config(mail_routes)

@main_routes.route('/')
def welcome():
    return "<h1>Twigelites Server!</h1>"

# Mail routes
@mail_routes.route('/mail')
def index(): 
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])
