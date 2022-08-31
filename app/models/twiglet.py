from audioop import add
from ..database.db import db
import datetime


class Twiglet(db.Model):
    twiglet_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    shop_name = db.Column(db.String)
    shop_id = db.Column(db.String)
    address = db.Column(db.String)
    found_by_user = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    votes = db.Column(db.Integer, default=0)
    date_found = db.Column(db.String)
    date_last_confirmed = db.Column(db.String)

    def __init__(self, longitude, latitude, shop_name, shop_id, address, found_by_user, date_found, date_last_confirmed):
        self.longitude = longitude
        self.latitude = latitude
        self.shop_name = shop_name
        self.shop_id = shop_id
        self.address = address
        self.found_by_user = found_by_user
        self.date_found = date_found
        self.date_last_confirmed = date_last_confirmed

    def serialize(self, ):
        return {
            "twiglet_id": self.twiglet_id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "shop_name": self.shop_name,
            "shop_id": self.shop_id,
            "address": self.address,
            "found_by_user": self.found_by_user,
            "votes": self.votes,
            "date_found": self.date_found,
            "date_last_confirmed": self.date_last_confirmed
        }

# we need a get user route
