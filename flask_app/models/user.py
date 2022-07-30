from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re

class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.ofAge = data['ofAge']
        self.legalToTrade = data['legalToTrade']
        self.mailingList = data['mailingList']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_new_user(cls, data):
        query = 'INSERT INTO users (email, username, password, ofAge, legalToTrade, mailingList, created_at, updated_at) VALUES (%(email)s,%(username)s,%(password)s,%(ofAge)s,%(legalToTrade)s,%(mailingList)s, NOW(), NOW());'
        return connectToMySQL('cryptowolves').query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL('cryptowolves').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_username(cls, data):
        query = 'SELECT * FROM users WHERE username = %(username)s;'
        result = connectToMySQL('cryptowolves').query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_session_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('cryptowolves').query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_form(data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']):
            flash('invalid email address!')
            is_valid = False
        if len(data['username']) < 3 and len(data['username']) <= 255:
            flash('Your username must be at least 3 characters long')
            is_valid = False
        if not 'ofAge' in data:
            flash('You did not confirm you are at least 18 years of age.')
            is_valid = False
        if not 'legalToTrade' in data:
            flash('You did not confirm it is legal for you to trade cryptocurrency.')
            is_valid = False
        if len(data['password']) < 8:
            flash('password must be atleast 8 characters')
            is_valid = False
        if data['password'] != data['passwordConfirm']:
            flash('Passwords must match')
            is_valid = False
        return is_valid