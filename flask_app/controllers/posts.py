from flask_app import app
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models.post import Post
from flask_app.models.user import User

@app.route('/market_watch')
def market_watch():
    if 'user_id' not in session:
        return redirect('/login')
    user_in_db = User.get_user_by_session_id({'id':session['user_id']})
    posts_info = Post.get_all_posts()
    session['user_id'] = user_in_db.id
    return render_template('MarketWatch.html', posts_info = posts_info, user_in_db=user_in_db)

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

@app.route('/post/delete/<int:id>')
def delete_post(id):
    if 'user_id' not in session:
        flash("You can't delete something if you're not logged in")
        return redirect('/login')
    Post.delete_post({'id':id})
    return redirect('/market_watch')