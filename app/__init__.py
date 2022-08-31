from dotenv import load_dotenv
from os import environ
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send, join_room

from .database.db import db
from .routes.main import main_routes
from .routes.auth import auth
from .routes.twiglet import twiglet
from flask_jwt_extended import JWTManager



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
socketio = SocketIO(app, cors_allowed_origins='*')

# Socket io

@socketio.on('connect')
def connect():
    join_room(request.values['id'])
    print("****CONNECTED!*****")

@socketio.on('disconnect')
def disconnect():
    print("****DISCONNECTED!*****")

@socketio.on('send-message')
def get_message(data):
    recipients = data['recipients']
    text = data['text']

    for recipient in recipients:
        new_recipients = [r for r in recipients if r!= recipient]
        new_recipients.append(request.values['id'])
        json_data = {
            "recipients": new_recipients, "sender": request.values['id'], "text":text
        }
        emit("receive-message", json_data, room=recipient)


app.register_blueprint(main_routes)
app.register_blueprint(auth)
app.register_blueprint(twiglet)


# app.register_blueprint(auth_routes, url_prefix='/auth')

# Main

if __name__ == "__main__":
    app.run(debug=True)

