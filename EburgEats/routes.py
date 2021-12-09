import secrets, os
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
    'location' : '1713 Canyon Rd, Ellensburg, WA 98926',
    }
]
hours = [
    {
    'mon' : '12-8:30PM',
    'tue' : '12-8:30PM',
    'wed' : '12-8:30PM',
    'thu' : '12-8:30PM',
    'fri' : '12-8:30PM',
    'sat' : '12-8:30PM',
    'sun' : 'CLOSED'
    }
]
# end of dummy post data

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/restaurantPage")
def restaurantPage():
    return render_template('restaurant_template.html', posts = posts, restaurants=restaurants, hours=hours)

@app.route("/photosPage")
def photosPage():
    return render_template('photos-page.html', restaurants=restaurants)

@app.route("/new_review", methods=['GET','POST'])
def new_review():
    form = ReviewForm()

    if form.validate_on_submit():
        review = Review(rating=request.form["rate"], review=form.review.data)
        db.session.add(review)
        db.session.commit()
        print('Your review has been posted!', 'success')
        return redirect('/restaurantPage')
    if request.method == 'POST':
        review = request.form["reviewPost"]
        return redirect(url_for("restaurantPage"))

    return render_template('write-a-review.html', title='New Review', form=form, legend='New Review',
    restaurants=restaurants)

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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/accountOverview/images', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@app.route("/account", methods=['GET','POST'])
def account():
    if current_user.is_authenticated == False:
        return redirect(url_for('login'))
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file= save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        print(form.username)
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='accountOverview/images/' + current_user.image_file)
    return render_template('accountOverview.html', user = current_user, image_file = image_file, form = form) 

@app.route("/favorites")
def favorites():
    if current_user.is_authenticated == False:
        return redirect(url_for('/login'))
    buis1 = Buisness(name='Seng Tong Thai Cuisine',genre='Thai',address='1713 Canyon Rd, Ellensburg, WA 98926',phone='(509) 993-2888',website='https://sengtongthaicuisine.com')
    buis2 = Buisness(name='Campus U-Tote-Em',genre='American',address='810 E University Way Ellensburg, WA 98926',phone='(509) 925-1600', website='http://campusutotem.com')
    buis3 = Buisness(name='Tacos Chalitos',genre='Mexican',address='209 S Main St, Ellensburg, WA 98926',phone='(509) 962-5643', website='http://tacoschalito.com')
    
    db.session.commit()
    image_file = url_for('static', filename='accountOverview/images/' + current_user.image_file)
    return render_template('myFavorites.html', user = current_user, image_file = image_file, buis1 = buis1, buis2 = buis2, buis3 = buis3)

@app.route("/myReviews")
def myreviews():
    if current_user.is_authenticated == False:
        return redirect(url_for('/login'))
    image_file = url_for('static', filename='accountOverview/images/' + current_user.image_file)
    return render_template('myReviews.html',  user = current_user, image_file = image_file)

##usally this is a button on the home page, will need to change how homepage looks after a user logs in
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


##
# Restaurants should use template for their page
# Allows users to post a reviw on to a Restaurant
# Restaurants should display information from db (restaurant info and user info assiociate with restaurant)