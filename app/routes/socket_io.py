
from flask_socketio import SocketIO, emit, send, join_room
from flask import request

def start_socket(socketio):

    @socketio.on('connect')
    def connect():
        print(request.values['id'])
        # join_room(request.values['id'])
        print("****CONNECTED!*****")

    @socketio.on('disconnect')
    def disconnect():
        print("****DISCONNECTED!*****")

    @socketio.on('join-chat')
    def join_chat(room):
        if room is not None:
           print("hiiii", room)
           join_room(room)


    @socketio.on('send-message')
    def get_message(data):
        recipients = data['recipients']
        text = data['text']
        print("RECIII", recipients)
        print("DATA", data)
        for recipient in recipients:
            print("RECIPIENTs", recipients)
            new_recipients = [r for r in recipients if r!= recipient]
            (type(recipient) == "string")
            new_recipients.append(request.values['id'])
            print("NEW RECIPIENTS", new_recipients)
            json_data = {
                    "recipients": new_recipients, "sender": request.values['id'], "text":text
                }
            emit("receive-message", json_data, to=recipient)
