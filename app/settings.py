# from os import environ
# from dotenv import load_dotenv
# # from os import environ
# from flask import Flask, render_template, request
# from flask_cors import CORS

# from .database.db import db
# from .routes.main import main_routes
# from .routes.auth import auth
# from .routes.twiglet import twiglet
# from flask_jwt_extended import JWTManager



# database_uri = environ.get('DATABASE_URL')

# if 'postgres:'in database_uri:
#     database_uri = database_uri.replace("postgres:", "postgresql:")



# #Set up the app
# app = Flask(__name__)
# app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET')  
# # Change this!
# jwt = JWTManager(app)

# # app.config.update(
# #     SQLALCHEMY_DATABASE_URI=database_uri,
# #     SQLALCHEMY_TRACK_MODIFICATIONS=environ.get(
# #         'SQLALCHEMY_TRACK_MODIFICATIONS')
# # )


# # import os 

# # SQLALCHEMY_DATABASE_URI=database_uri, SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
