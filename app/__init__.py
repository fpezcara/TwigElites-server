from dotenv import load_dotenv
from os import environ
from flask import Flask, render_template, request
from flask_cors import CORS

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth
from .routes.twiglet import twiglet

from flask_jwt_extended import JWTManager
from flask import Flask, current_app


# Load environment variables
load_dotenv()

# database_uri = environ.get('DATABASE_URL')

# if 'postgres:'in database_uri:
#     database_uri = database_uri.replace("postgres:", "postgresql:")


# Set up the app

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET')  # Change this!
    jwt = JWTManager(app)
    # app.config.update(
    #     SQLALCHEMY_DATABASE_URI=database_uri,
    #     SQLALCHEMY_TRACK_MODIFICATIONS=environ.get(
    #         'SQLALCHEMY_TRACK_MODIFICATIONS')
    # )
    app.config.from_pyfile(config_file)

    CORS(app)
    db.app = app
    db.init_app(app)

    app.register_blueprint(main_routes)
    app.register_blueprint(auth)
    app.register_blueprint(twiglet)

    return app

# app.register_blueprint(auth_routes, url_prefix='/auth')

# Main

    if __name__ == "__main__":
        app.run(debug=True)

