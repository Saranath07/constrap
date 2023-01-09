from .database import db


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String(255))
    name = db.Column(db.String, nullable = False)
    
    phone_number = db.Column(db.Text)
    
    




class Shops(db.Model):
    __tablename__ = "Shops"
    sid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    sname = db.Column(db.String, nullable = False)
    slocality = db.Column(db.String)
    sdescription = db.Column(db.String)
    saddress = db.Column(db.String)
    notc = db.Column(db.Integer)
    imgloc = db.Column(db.String)
    scontact = db.Column(db.String)



