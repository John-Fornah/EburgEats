from sqlalchemy.orm import relationship
from EburgEats import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy_utils import aggregated

## If models gets modify, you need to modify the table in the db as well
## since we don't have user info (at the time of writing this) easier to recreate db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## this class represents a table on the database
class Buisness(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(75), unique=True, nullable=False)
    phone = db.Column(db.String(12), unique=True)
    website = db.Column(db.String(50))

    def __repr__(self): ##define how a user object is printed
        return f"Buisness('{self.name}')"

class Review(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    idRating = db.Column('idRating', db.Integer, nullable=False)
    textContext = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idUser = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    idBuisness = db.Column(db.Integer,db.ForeignKey('buisness.id'), nullable=False)

    #function to mapper Review to starRating
    starRatings = relationship("starRatings", backref="Review", uselist=False)

    def __repr__(self): 
        return f"Review('{self.rating}','{self.textContext}','{self.date}')"

    ##@aggregated('ratings', db.Column(db.Integer))
    ##def average_rating(self):
    ##    return db.func.avg(starRatings.rating)

class starRatings(db.Model):
    id = db.Column('idRating', db.Integer, db.ForeignKey('review.id'), primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"rating('{self.rating}')"

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(35), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='placeholder.png')
    
    reviews = db.relationship('Review', backref='User', lazy=True)

    def __repr__(self): ##define how a user object is printed
        return f"User('{self.username}','{self.password}','{self.email}')"
  