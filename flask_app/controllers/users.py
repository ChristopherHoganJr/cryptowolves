from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    if 'user_id' not in session:
        user_in_db = 'user isnt logged in'
    else:
        user_in_db = User.get_user_by_session_id({'id':session['user_id']})
    return render_template('Landing.html', user_in_db=user_in_db)

@app.route('/create_account')
def create_account():
    if 'user_id' in session:
        del session['user_id']
    return render_template('CreateAccount.html')

@app.route('/login')
def login():
    if 'user_id' in session:
        del session['user_id']
    return render_template('Login.html')

@app.route('/create_account/register', methods=['post'])
def register_account():
    # Run through initial validation checks
    if not User.validate_form(request.form):
        return redirect('/create_account')
    # Check if the the email has already been registered
    email_in_db = User.get_user_by_email({'email':request.form['email']})
    if email_in_db:
        flash('That email already exists')
        return redirect('/create_account')
    # Check if the username has already been taken
    username_in_db = User.get_user_by_username({'username':request.form['username']})
    if username_in_db:
        flash('That username already exists')
        return redirect('/create_account')
    # Check if to add user to the mailing list
    if 'mailingList' not in request.form:
        onMailingList = 0
    else:
        onMailingList = 1
    # If all checks are clear, encrypt password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # data to push to database
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'password': pw_hash,
        'ofAge': request.form['ofAge'],
        'legalToTrade': request.form['legalToTrade'],
        'mailingList': onMailingList
    }

    # Create new user
    # Push user id to session id
    user_id = User.create_new_user(data)
    session['user_id'] = user_id
    return redirect('/market_watch')

@app.route('/login/authenticate', methods=['post'])
def login_user():
    user_in_db = User.get_user_by_email({'email': request.form['email']})

    if not user_in_db:
        flash('EMAIL DOESNT MATCH')
        return redirect('/login')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('PASSWORD DOESNT MATCH')
        return redirect('/login')

    session['user_id'] = user_in_db.id
    return redirect('/market_watch')