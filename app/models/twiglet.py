from ..database.db import db
import datetime


class Twiglet(db.Model):
    twiglet_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    shop_name = db.Column(db.String)
    address = db.Column(db.String)
    found_by_user = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    date_found = db.Column(db.Date)
    date_last_confirmed = db.Column(db.Date)

