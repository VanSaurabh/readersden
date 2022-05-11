from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request
from werkzeug.security import check_password_hash

from src.service import user_service
from src.util import util


def login_by_username_password():
    auth = request.form
    return None \
        if not auth or not auth.get('username') or not auth.get('password') \
        else get_token(auth)


def get_token(auth):
    username = auth.get('username')
    password = auth.get('password')
    user_details = user_service.get_user_by_username(username)

    return prepare_token(username) \
        if check_password_hash(user_details.password, password=password) \
        else None


def prepare_token(username):
    return jwt.encode(
        {
            'userId': username,
            'exp': datetime.utcnow() + timedelta(minutes=get_jwt_expiration_mins())
        }, get_jwt_secret()
    )


def token_verifier(func):
    @wraps(func)
    def verify_jwt(*args, **kwargs):
        token = request.headers.get('X-Access-Token')
        if token is None:
            return {'error': 'Token is required !'}, 401, {'Content-Type': 'application/json'}
        else:
            try:
                data = jwt.decode(token, get_jwt_secret())
                check_valid_user(data['userId'])
            except jwt.ExpiredSignatureError:
                return {'error': 'Token expired !'}, 401, {'Content-Type': 'application/json'}
            except:
                return {'error': 'Invalid token !'}, 401, {'Content-Type': 'application/json'}

            return func(*args, **kwargs)

    return verify_jwt


def check_valid_user(user_id):
    user = user_service.get_user_by_username(user_id)
    if user is None:
        raise Exception


def get_jwt_secret():
    return util.get_config()["jwt"]["token"]["secret"]


def get_jwt_expiration_mins():
    return util.get_config()["jwt"]["token"]["expiration"]
