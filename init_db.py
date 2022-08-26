from app import db
# from app.models.listing import Listing

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
