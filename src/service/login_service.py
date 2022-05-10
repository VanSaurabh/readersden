from datetime import datetime, timedelta

import jwt
from flask import request
from werkzeug.security import check_password_hash

import src.util.util
from src.service import user_service


def login_by_username_password():
    auth = request.form
    return None \
        if not auth or not auth.get('username') or not auth.get('password') \
        else get_token(auth)


def get_token(auth):
    username = auth.get('username')
    password = auth.get('password')
    user_details = user_service.get_user_by_username(username)
    jwt_config = src.util.util.read_config('config.yml')

    return prepare_token(jwt_config, username) \
        if check_password_hash(user_details.password, password=password) \
        else None


def prepare_token(jwt_config, username):
    return jwt.encode(
        {
            'userId': username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, jwt_config["jwt"]["token"]["secret"]
    )
