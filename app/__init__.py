from dotenv import load_dotenv
from os import environ
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth
from .routes.twiglet import twiglet
from flask_jwt_extended import JWTManager
from .routes.socket_io import start_socket



# Load environment variables
load_dotenv()

database_uri = environ.get('DATABASE_URL')

if 'postgres:'in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")


# Set up the app

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET')
jwt = JWTManager(app)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)
db.app = app
db.init_app(app)

# Socket io
socketio = SocketIO(app, cors_allowed_origins='*')
start_socket(socketio)


app.register_blueprint(main_routes)
app.register_blueprint(auth)
app.register_blueprint(twiglet)


# app.register_blueprint(auth_routes, url_prefix='/auth')

# Main

if __name__ == "__main__":
    app.run(debug=True)

