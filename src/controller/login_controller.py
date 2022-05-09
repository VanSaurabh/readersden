from src.service.login_service import login_by_username_password
from flask import make_response, jsonify


def login():
    token = login_by_username_password()
    if not token:
        return make_response(jsonify({'error': 'wrong username or password !'}), 403)
    else:
        return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
