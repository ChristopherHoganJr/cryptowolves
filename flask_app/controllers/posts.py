from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.post import Post
from flask_app.models.user import User

@app.route('/market_watch')
def market_watch():
    # Check if user is logged in
    if 'user_id' not in session:
    #     # if user is NOT logged in, redirect to login page
        return redirect('/login')
    # grab user profile by id
    user_in_db = User.get_user_by_session_id({'id':session['user_id']})
    # pull all posts from all users
    posts_info = Post.get_all_posts()
    # return page with items
    session['user_id'] = user_in_db.id
    return render_template('MarketWatch.html', posts_info = posts_info)

@app.route('/post/submit', methods=['post'])
def submit_post():
    user_in_db = User.get_user_by_session_id({'id':session['user_id']})
    data = {
        'post': request.form['input-post'],
        'category': 'btc',
        'users_id': user_in_db.id
    }
    Post.create_new_post(data)
    return redirect('/market_watch')