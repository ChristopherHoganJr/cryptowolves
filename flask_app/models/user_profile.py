from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app import app
from flask import flash

class User_Profile:
    def __init__(self,data):
        self.profile_id = data['profile_id']
        self.profile_name = data['profile_name']
        self.profile_about = data['profile_about']
        self.profile_favorite_project = data['profile_favorite_project']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def pull_user_profile(cls, data):
        query = 'SELECT * FROM users_profile JOIN users ON users_profile.users_id = users.id WHERE id=%(id)s;'
        results = connectToMySQL('cryptowolves').query_db(query, data)
        print(results)
        return results

    @classmethod
    def pull_all_user_profile(cls):
        query = 'SELECT * FROM users_profile JOIN users ON users_profile.users_id = users.id;'
        results = connectToMySQL('cryptowolves').query_db(query)
        all_users = []
        for single_user in results:
            user_info = {
                'profile_id': single_user['profile_id'],
                'profile_name': single_user['profile_name'],
                'profile_about':single_user['profile_about'],
                'profile_favorite_project':single_user['profile_favorite_project'],
                'profile_username':single_user['username']
            }
            all_users.append(user_info)
        return all_users

    @classmethod
    def push_user_profile(cls, data):
        query = 'INSERT INTO users_profile (profile_name, profile_about, profile_favorite_project, users_id, created_at, updated_at) VALUES (%(profile_name)s,%(profile_about)s, %(profile_favorite_project)s, %(users_id)s, NOW(),NOW());'
        return connectToMySQL('cryptowolves').query_db(query, data)

    @classmethod
    def edit_user_profile(cls, data):
        query = 'UPDATE users_profile SET profile_name = %(profile_name)s, profile_about = %(profile_about)s, profile_favorite_project = %(profile_favorite_project)s, updated_at = NOW() WHERE users_id = %(users_id)s;'
        return connectToMySQL('cryptowolves').query_db(query, data)