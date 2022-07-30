from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_profile import User_Profile
from flask_app.models.user import User

@app.route('/user/profile/create')
def user_create_page():
    if 'user_id' not in session:
        return redirect('/login')
    profileData = User_Profile.pull_user_profile({'id':session['user_id']})
    return render_template('CreateUserProfile.html')

@app.route('/user/profile/create/submit', methods=['post'])
def user_create_submit():
    if 'user_id' not in session:
            return redirect('/login')
    profileData = {
        'profile_name':request.form['profile_name'],
        'profile_about':request.form['profile_about'],
        'profile_favorite_project':request.form['profile_favorite_project'],
        'users_id': session['user_id']
    }
    User_Profile.push_user_profile(profileData)
    return redirect('/market_watch')

@app.route('/user/profile/edit')
def user_edit_page():
    if 'user_id' not in session:
        return redirect('/login')
    profileData = User_Profile.pull_user_profile({'id':session['user_id']})
    return render_template('EditUserProfile.html', profileData = profileData)

@app.route('/user/profile/edit/submit', methods=['post'])
def user_edit_submit():
    if 'user_id' not in session:
            return redirect('/login')
    profileData = {
        'profile_name':request.form['profile_name'],
        'profile_about':request.form['profile_about'],
        'profile_favorite_project':request.form['profile_favorite_project'],
        'users_id': session['user_id']
    }
    User_Profile.edit_user_profile(profileData)
    return redirect(f"/user/profile/{session['user_id']}")

@app.route('/user/profile/<int:id>')
def user_profile(id):
    profileData = User_Profile.pull_user_profile({'id':id})
    return render_template('UserProfile.html', profileData = profileData)

@app.route('/users/all_wolves')
def get_all_profiles():
    if 'user_id' not in session:
        return redirect('/login')
    users_in_db = User_Profile.pull_all_user_profile()
    return render_template('AllUsers.html', users_in_db=users_in_db)

