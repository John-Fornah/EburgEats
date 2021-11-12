from EburgEats import db
from datetime import datetime

## this class represents a table on the database
class BuisnessGenre(db.Model): 
    idBuisness = db.Column('idBuisness', db.Integer, db.ForeignKey('buisness.idBuisness'), primary_key=True, nullable=False)
    idGenre = db.Column('idGenre', db.Integer, db.ForeignKey('genre.idGenre'), primary_key=True)

class Buisness(db.Model): 
    idBuisness = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)

    Genres = db.relationship("BuisnessGenre", backref='Buisness', lazy=True)

    def __repr__(self): ##define how a user object is printed
        return f"Buisness('{self.name}')"

class Genre(db.Model): 
    idGenre = db.Column(db.Integer, primary_key=True)
    genreName = db.Column(db.String(20), unique=True, nullable=False)

    Buisnesses = db.relationship("BuisnessGenre", backref='Genre', lazy=True)

    def __repr__(self): 
        return f"Genre('{self.genreName}')"

class Review(db.Model): 
    idReview = db.Column(db.Integer, primary_key=True)
    idRating = db.Column('idRating', db.Integer, db.ForeignKey('starRatings.idRating'), nullable=False)
    textContext = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    idUser = db.Column(db.Integer,db.ForeignKey('user.idUser'), nullable=False)

    def __repr__(self): 
        return f"Review('{self.rating}','{self.textContext}','{self.date}')"

class starRatings(db.Model):
    idRating = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    idReview = db.Column('idReview', db.Integer, db.ForeignKey('review.idReview'), nullable=False)

    def __repr__(self):
        return f"rating('{self.rating}')"

class User(db.Model): 
    idUser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(35), nullable=False)
    
    reviews = db.relationship('Review', backref='User', lazy=True)

    def __repr__(self): ##define how a user object is printed
        return f"User('{self.username}','{self.password}','{self.email}')"

