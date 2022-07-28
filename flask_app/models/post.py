from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app import app
from flask import flash

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.post = data['post']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def create_new_post(cls, data):
        query = 'INSERT INTO posts (post, category, created_at, updated_at, users_id) VALUES (%(post)s,%(category)s,NOW(),NOW(),%(users_id)s);'
        return connectToMySQL('web3Wolves').query_db(query, data)

    @classmethod
    def get_all_posts(cls):
        query = 'SELECT * FROM posts JOIN users ON posts.users_id = users.id ORDER BY posts.id DESC'
        results = connectToMySQL('web3Wolves').query_db(query)
        discussion_posts = []
        for single_post in results:
            print(single_post['id'])
            discussion_post = {
                'post_id': single_post['id'],
                'username': single_post['username'],
                'post':single_post['post'],
                'user_id':single_post['users.id']
            }
            discussion_posts.append(discussion_post)
        return discussion_posts

    @classmethod
    def delete_post(cls,data):
        query = 'DELETE FROM posts WHERE id=%(id)s;'
        return connectToMySQL('web3Wolves').query_db(query, data)