from urllib import response
from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from ..database.db import db
from ..models.twiglet import Twiglet
from werkzeug import exceptions
import datetime


twiglet = Blueprint("twiglet", __name__)

#? 1. add a new twiglet to our db
#? 2. if twiglet location already exists, then update only "date_last_confirmed"
#? 3. delete twiglet from db
#? 4. route to filter twiglets by location

@twiglet.route('/twiglets', methods=['GET', 'POST'])
@jwt_required()
# gets all twiglets and adds a new one to our route
def get_all_twiglets():
    # print(get_jwt_identity())
    if request.method == "GET":
        try:
            all_twiglets = Twiglet.query.all()
            response = jsonify([e.serialize() for e in all_twiglets]) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response      
        except exceptions.NotFound:
            raise exceptions.NotFound("Twiglet not found!")
    elif request.method == "POST":
        all_twiglets = Twiglet.query.all()
        req = request.get_json()
        longitude = req['longitude']
        latitude = req['latitude']
        shop_name = req['shop_name']
        address = req['address']
        found_by_user = req['found_by_user']
        date_found = req['date_found']
        date_last_confirmed = req['date_found']
     

        existing_location = Twiglet.query.filter_by(latitude=latitude, longitude=longitude).first()
        if existing_location:
            existing_location.date_last_confirmed = datetime.datetime.utcnow()
            db.session.add(existing_location)
            db.session.commit()
            return jsonify("Tiglet was updated!"), 201
        new_twiglet = Twiglet(longitude=longitude, latitude=latitude, shop_name=shop_name, address=address, found_by_user=found_by_user, date_found=date_found, date_last_confirmed=date_last_confirmed)       

        db.session.add(new_twiglet)
        db.session.commit()

        return jsonify("New twiglet was added!"), 201


@twiglet.route('/twiglets/<int:twiglet_id>/', methods=['GET', 'DELETE'])
def get_twiglet_id(twiglet_id):
# get a Twiglet by its id  
    if request.method == 'GET':
        try:
            twig = Twiglet.query.get_or_404(twiglet_id)
            response = jsonify([twig.serialize()]) 
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except exceptions.NotFound:
            raise exceptions.NotFound("Twiglet not found!")
        except:
            raise exceptions.InternalServerError()

# Deletes a Twiglet by its id 
    elif request.method == 'DELETE':
        try:
            delete_twiglet = Twiglet.query.get_or_404(twiglet_id)

            db.session.delete(delete_twiglet)
            db.session.commit()
            return "A twiglet was sucessfully deleted!", 204
        except exceptions.NotFound:
            # message appears when you search on postman - DELETE
            raise exceptions.NotFound("Twiglet not found!")
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
