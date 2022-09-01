
from flask_socketio import SocketIO, emit, send, join_room
from flask import request

def start_socket(socketio):

    @socketio.on('connect')
    def connect():
        print(request.values['id'])
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
            print(recipient)
            new_recipients = [r for r in recipients if r!= recipient]
            (type(recipient) == "string")
            new_recipients.append(request.values['id'])
            print(new_recipients)
            json_data = {
                    "recipients": new_recipients, "sender": request.values['id'], "text":text
                }
            print(json_data)
            emit("receive-message", json_data, to=recipient)
