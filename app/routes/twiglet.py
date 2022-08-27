from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from ..database.db import db
from ..models.user import User
from werkzeug import exceptions


twiglet = Blueprint("twiglet", __name__)

#? 1. add a new twiglet to our db
#? 2. if twiglet location already exists, then update only "date_last_confirmed"
#? 3. delete twiglet from db
#? 4. route to filter twiglets by location
