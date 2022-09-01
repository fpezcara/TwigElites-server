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
    date_found = db.Column(db.Date)
    date_last_confirmed = db.Column(db.Date)

    def serialize(self):
        return {
            "twiglet_id": self.twiglet_id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "shop_name": self.shop_name,
            "shop_id": self.shop_id,
            "address": self.address,
            "found_by_user": self.found_by_user,
            "votes": self.votes,
            "date_found": number_of_days(self.date_found, datetime.date.today()),
            "date_last_confirmed": number_of_days(self.date_last_confirmed, datetime.date.today())
        }

def number_of_days(date_1, date_2):  
    calculation = (date_1 + date_2).days
    return f"{calculation}"


# we need a get user route
