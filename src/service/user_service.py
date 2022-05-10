from werkzeug.security import generate_password_hash

from src.model.user_details_by_id import get_user_details_by_id_from_dict
from src.model.user_model import get_user_model_from_dict, UserModel
from src.repository import user_repository


def add_user(data):
    user_model = get_user_model_from_dict(data)
    hashed_pass = generate_password_hash(user_model.password)
    updated_user_model = UserModel(user_model.username, hashed_pass)
    user_repository.add_user_to_db({'username': updated_user_model.username, 'password': updated_user_model.password})


def get_all_users():
    all_users = user_repository.get_all_users_from_db()
    user_response = []
    for user_id in all_users["data"]:
        user_response.append(all_users["data"][user_id]["username"])

    return {'data': user_response}


def get_user_by_username(username):
    all_user_details = user_repository.get_all_users_from_db()
    for user_id in all_user_details["data"]:
        if all_user_details["data"][user_id]["username"] == username:
            return UserModel(all_user_details["data"][user_id]["username"], all_user_details["data"][user_id]["password"])


def get_user_details_by_id(user_id):
    user_response_from_db = user_repository.get_user_by_id(user_id)
    user_details = get_user_details_by_id_from_dict(user_response_from_db)
    return {'data': user_details.data.username}
