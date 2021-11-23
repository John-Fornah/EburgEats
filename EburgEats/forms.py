from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from EburgEats.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=35)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=25)])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    ## Custom validation to prevent user from creating an account with a taken username or Email
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already being used.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=25)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ReviewForm(FlaskForm):
    rating = RadioField('Rating', coerce=int, choices=[('1','one star'),('2','two stars'),('3','three stars'),('4','four stars'),('5','five stars')])
    review = TextAreaField('Review', validators=[DataRequired(), Length(min=5, max=500)])
    submit = SubmitField('Submit')