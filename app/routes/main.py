from flask import Blueprint

main_routes = Blueprint("main", __name__)

@main_routes.route('/')
def welcome():
    return "Twigelites Server!"
