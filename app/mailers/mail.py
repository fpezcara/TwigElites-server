from flask import Flask
from flask import Blueprint, request, render_template, jsonify
from app.mailers import mail_config
from flask_mail import Mail
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required


main_routes = Blueprint("main", "config", __name__)
mail_routes = Blueprint("mail", "config", __name__)
mail = mail_config(mail_routes)


def mail_config(app):
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '9e5ea2f8051c1c'
    app.config['MAIL_PASSWORD'] = 'f95843dfc60972'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    return Mail(app)

@main_routes.route('/')
def welcome():
    return "<h1>Twigelites Server!</h1>"

# Mail routes
@mail_routes.route('/mail', methods=['GET', 'POST'])
def index(): 
    # if request.methods == 'POST':
    #     mail = mail_config(mail_routes)
    #     msg = Message("A new Twiglet has been found!", )
    #     mail.send(msg)
    return "hi"


from flask_mail import Mail

def mail_config(app):
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = '9e5ea2f8051c1c'
    app.config['MAIL_PASSWORD'] = 'f95843dfc60972'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    return Mail(app)
