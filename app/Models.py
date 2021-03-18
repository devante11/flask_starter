from . import db

class Property(db.Model):

    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String())
    description = db.Column(db.String())
    rooms = db.Column(db.String())
    bathrooms=db.Column(db.String())
    price = db.Column(db.String())
    prop_type = db.Column(db.String())
    location = db.Column(db.String())
    photo = db.Column(db.String())
    

    def __init__(self, title, description, Rooms, Bathrooms, Price, Prop_type, Location,Photo):
        self.Title=title
        self.Description=description
        self.Rooms=rooms
        self.Bathrooms=bathrooms
        self.Price=price
        self.Prop_type=prop_type
        self.Location=location
        self.Photo=photo