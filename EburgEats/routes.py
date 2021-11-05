from flask import Flask, render_template, url_for
from EburgEats import app
from EburgEats.models import User, Review, Buisness, Genre, BuisnessGenre

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/template")
def template():
    return render_template('restaurant_template.html')

@app.route("/login",methods=['GET','POST'])
def login():
    return render_template('login-page.html')


## db work
##
# Restaurants should use template for their page
# Allow users to create accounts and login
# Allows users to post a reviw on to a Restaurant
# Restaurants should display information from db (restaurant info and user info assiociate with restaurant)