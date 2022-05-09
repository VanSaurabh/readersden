from datetime import datetime, timedelta
from werkzeug.security import check_password_hash

import jwt
from flask import request

import src.util.util
from src.service import user_service


def login_by_username_password():
    auth = request.form

    if not auth or not auth.get('username') or not auth.get('password'):
        return None
    else:
        username = auth.get('username')
        password = auth.get('password')

    user_details = user_service.get_user_by_username(username)

    jwt_config = src.util.util.read_config('config.yml')

    if check_password_hash(user_details.password, password=password):
        return jwt.encode(
            {
                'userId': username,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            },
            jwt_config["jwt"]["token"]["secret"]
        )
    else:
        return None
