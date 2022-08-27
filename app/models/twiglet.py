from ..database.db import db
import datetime


class Twiglet(db.Model):
    twiglet_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    shop_name = db.Column(db.String)
    address = db.Column(db.String)
    found_by_user = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    date_found = db.Column(db.String)
    date_last_confirmed = db.Column(db.String)

    def serialize(self):
        return {
            "twiglet_id": self.twiglet_id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "shop_name": self.shop_name,
            "address": self.address,
            "found_by_user": self.found_by_user,
            "date_found": self.date_found,
            "date_last_confirmed": self.date_last_confirmed
        }

    # def get_by_id(self):
        

# we need a get user route
