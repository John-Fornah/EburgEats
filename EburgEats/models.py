from sqlalchemy.orm import relationship
from EburgEats import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy_utils import aggregated

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## this class represents a table on the database
class BuisnessGenre(db.Model): 
    idBuisness = db.Column('idBuisness', db.Integer, db.ForeignKey('buisness.id'), primary_key=True, nullable=False)
    idGenre = db.Column('idGenre', db.Integer, db.ForeignKey('genre.id'), primary_key=True)

class Buisness(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    Genres = db.relationship("BuisnessGenre", backref='Buisness', lazy=True)

    @aggregated('ratings', db.Column(db.Integer))
    def average_rating(self):
        return db.func.avg(starRatings.rating)

    ratings = db.relationship('starRatings')

    def __repr__(self): ##define how a user object is printed
        return f"Buisness('{self.name}')"

class Genre(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    genreName = db.Column(db.String(20), unique=True, nullable=False)

    Buisnesses = db.relationship("BuisnessGenre", backref='Genre', lazy=True)

    def __repr__(self): 
        return f"Genre('{self.genreName}')"

class Review(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    idRating = db.Column('idRating', db.Integer, nullable=False)
    review = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idUser = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    #function to mapper Review to starRatings
    rating = relationship("starRatings", backref="Review", uselist=False)

    def __repr__(self):
        return f"Review('{self.rating}','{self.review}','{self.date}')"


class starRatings(db.Model):
    id = db.Column('idRating', db.Integer, db.ForeignKey('review.id'), primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)

    idReview = db.Column(db.Integer, db.ForeignKey(Review.id))

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
