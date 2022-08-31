from flask import Blueprint

main_routes = Blueprint("main", __name__)

@main_routes.route('/')
def welcome():
    return "<h1>Twigelites Server!</h1>"





