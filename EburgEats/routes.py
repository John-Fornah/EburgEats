from flask import Flask, render_template, url_for, request, flash, redirect
from EburgEats import app, db, bcrypt
from EburgEats.forms import LoginForm, RegistrationForm, ReviewForm
from EburgEats.models import User, Review, Buisness, Genre, BuisnessGenre, starRatings
from flask_login import login_user, current_user, logout_user

#dummy data
posts = [
    {
    'username' : 'No Face',
    'rating' : '5',
    'date': "11/21/2021",
    'review': " SERIOUSLY SWEAR BY THIS PLACE!! Pad Thai is always spot on, the chicken is fantastic, fresh prawn rolls extra peanut sauce... and the Thai iced tea... UNBELIEVABLE!! Best Thai in town hands down. I've never had an issue with any takeout order. This business is fast and efficient! This is most definitely the best Thai I've had!  its my 9 th take out order and again... I'll be back! Thank you Seng Tong Thai!"
    }
]
restaurants = [
    {
    'name' : 'Seng Tong Thai Cuisine',
    'cuisine' : 'Thai',
    'phone' : '(509) 933-2888',
    'website' : 'https://sengtongthaicuisine.com',
    'location' : '1713 Canyon Rd, Ellensburg, WA 98926'
    }
]
# end of dummy post data

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/restaurantPage")
def restaurantPage():
    return render_template('restaurant_template.html', posts = posts, restaurants=restaurants)

@app.route("/photosPage")
def photosPage():
    return render_template('photos-page.html', restaurants=restaurants)

@app.route("/new_review", methods=['GET','POST'])
def new_review():
    form = ReviewForm()

#     if form.validate_on_submit():
#         review = Review(rating=request.form["rate"], review=form.review.data)
#         db.session.add(review)
#         db.session.commit()
#         flash('Your review has been posted!', 'success')
#         return redirect('/restaurantPage')
#     if request.method == 'POST':
#         review = request.form["reviewPost"]
#         return redirect(url_for("restaurantPage"))

    return render_template('write-a-review.html', title='New Review', form=form, legend='New Review', restaurants=restaurants)

@app.route("/login",methods=['GET','POST'])
def login():
    # a logged in user doesnt need access to the login or register page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        #login if user with inputted username and password exist in db
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            print('login Successful')
            return redirect(url_for('home'))
        else:
            print('Failed login')
    return render_template('login-page.html', form=form)

@app.route("/register",methods=['GET','POST'])
def register():
     # a logged in user doesnt need access to the login or register page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        print("account created you can now log in") # layouts dont show a success atm
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/account")
def account():
    return render_template('accountOverview.html')

@app.route("/favorites")
def favorites():
    return render_template('myFavorites.html')

@app.route("/myReviews")
def myreviews():
    return render_template('myReviews.html')

##usally this is a button on the home page, will need to change how homepage looks after a user logs in
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


##
# Restaurants should use template for their page
# Allows users to post a reviw on to a Restaurant
# Restaurants should display information from db (restaurant info and user info assiociate with restaurant)