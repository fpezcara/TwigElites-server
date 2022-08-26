from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


main_routes = Blueprint("main", __name__)

@main_routes.route('/')
def welcome():
    return "Twigelites Server!"




