
from flask_socketio import SocketIO, emit, send, join_room
from flask import request

def start_socket(socketio):

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
