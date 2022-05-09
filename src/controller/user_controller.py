from flask import request

from src.service import user_service


def add_user():
    """
        the endpoint creates a user
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        user_service.add_user(request.json)
        return "User is created !", 201, {'Content-Type': 'application/json'}
    else:
        raise 'Content type not supported !'


def get_all_users():
    """
        returns a list of all users from database
    """
    return user_service.get_all_users(), 200, {'Content-Type': 'application/json'}


def get_user_by_id(user_id):
    """
        returns user details by id
    """
    return user_service.get_user_details_by_id(user_id), 200, {'Content-Type': 'application/json'}