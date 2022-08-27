from ..database.db import db


class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    reputation = db.Column(db.Integer, nullable=True)

    def single_user(self):
        return { 
            "id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "reputation": self.reputation,
            }
    
