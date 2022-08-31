from ..database.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password_hash = db.Column(db.String(180), nullable=False)
    reputation = db.Column(db.Integer, nullable=True)

    def __init__(self, username, email, password_hash, reputation):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.reputation = reputation

    def single_user(self):
        if self is None:
            return "User doesn't exist!"
        return { 
            "id": self.user_id,
            "username": self.username,
            "email": self.email,
            "reputation": self.reputation,
            }

   
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute!")


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
