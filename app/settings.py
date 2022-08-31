from os import environ

database_uri = environ.get('DATABASE_URL')

if 'postgres:'in database_uri:
    database_uri = database_uri.replace("postgres:", "postgresql:")

# app.config.update(
#         SQLALCHEMY_DATABASE_URI=database_uri,
#         SQLALCHEMY_TRACK_MODIFICATIONS=environ.get(
#             'SQLALCHEMY_TRACK_MODIFICATIONS')
#     )

SQLALCHEMY_DATABASE_URI=database_uri
SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    
