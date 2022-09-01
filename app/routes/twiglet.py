from urllib import response
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from ..database.db import db
from ..models.twiglet import Twiglet
from ..models.user import User

from werkzeug import exceptions
import datetime


twiglet = Blueprint("twiglet", __name__)

@twiglet.route('/twiglets', methods=['GET', 'POST'])
@jwt_required(optional=True)
def get_all_twiglets():
    if request.method == "GET":
        try:
            all_twiglets = Twiglet.query.all()
            response = jsonify([e.serialize() for e in all_twiglets]) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response      
        except exceptions.NotFound:
            raise exceptions.NotFound("Twiglet not found!")
    elif request.method == "POST":
        user_identity = get_jwt_identity()
        current_user = User.query.filter_by(username=user_identity).first()
        all_twiglets = Twiglet.query.all()
        req = request.get_json()
        longitude = req['longitude']
        latitude = req['latitude']
        shop_name = req['shop_name']
        address = req['address']
        shop_id = req['shop_id']
   
        if user_identity is None:
            return jsonify("You're not authorised to add new twiglets. Create an account!"), 401
        existing_location = Twiglet.query.filter_by(latitude=latitude, longitude=longitude).first()
        # from this to this 10 miles radius
        if existing_location:
            existing_location.date_last_confirmed = datetime.date.today()
            db.session.add(existing_location)
            db.session.commit()
            return jsonify("Twiglet was updated!"), 201
        new_twiglet = Twiglet(longitude=longitude, latitude=latitude, shop_name=shop_name, address=address, found_by_user=current_user.user_id, date_found=datetime.date.utcnow(), date_last_confirmed=datetime.date.utcnow())  
  
        db.session.add(new_twiglet)
        db.session.commit()

        return jsonify("New twiglet was added!"), 201


@twiglet.route('/twiglets/<int:twiglet_id>/', methods=['GET', 'DELETE', 'PATCH'])
def get_twiglet_id(twiglet_id):

# get a Twiglet by its id  
    if request.method == 'GET':
        try:
            twig = Twiglet.query.get_or_404(twiglet_id)
            response = jsonify([twig.serialize()]) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            return jsonify("Twiglet not found!"), 201
        except:
            raise exceptions.InternalServerError()

# Deletes a Twiglet by its id - NEED TO FIX MESSAGE TO SEND ONCE ITS DELETED!
    elif request.method == 'DELETE':
        try:
            delete_twiglet = Twiglet.query.get_or_404(twiglet_id)
            db.session.delete(delete_twiglet)
            db.session.commit()

            return "A twiglet was successfully deleted!", 200
        except exceptions.NotFound:
            # message appears when you search on postman - DELETE
            raise exceptions.NotFound("Twiglet not found!")
        except:
            raise exceptions.InternalServerError()
    
    elif request.method == 'PATCH':
        try:

            twiglet = Twiglet.query.get_or_404(twiglet_id)
            twiglet.votes = twiglet.votes + 1
            db.session.add(twiglet)
            db.session.commit()
         
            return "Twiglet's vote added!"
        except:   
            raise exceptions.InternalServerError()
            

@twiglet.route('/twiglets/user/<int:user_id>', methods=['GET'])
def get_twiglet_by_user(user_id):
    if request.method == 'GET':
        try:
            twig = Twiglet.query.filter_by(found_by_user=user_id).all()
            response = jsonify([t.serialize() for t in twig])
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            return jsonify("User's twiglet not found!")
        except:
            raise exceptions.InternalServerError()
  

# Exception Handlers

@twiglet.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@twiglet.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@twiglet.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us!"}, 500
