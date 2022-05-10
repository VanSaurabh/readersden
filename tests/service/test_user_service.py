from src.model.user_model import UserModel
from src.service.user_service import add_user, get_all_users, get_user_by_username, get_user_details_by_id


def test_add_user(mocker):
    user_model = UserModel('sample', 'pass')
    mocker.patch('src.model.user_model.get_user_model_from_dict', return_value=user_model)
    mocker.patch('src.repository.user_repository.add_user_to_db', return_value=None)
    data = {'username': 'sample', 'password': 'pass'}
    add_user(data)


def test_get_all_users(mocker):
    mocker.patch('src.repository.user_repository.get_all_users_from_db', return_value=all_user_data())
    all_users = get_all_users()
    assert all_users.get("data") == ['sample', 'sample1', 'sample2']


def test_get_user_by_username(mocker):
    mocker.patch('src.repository.user_repository.get_all_users_from_db', return_value=all_user_data())
    user_model = get_user_by_username("sample")
    assert user_model.username == "sample"
    assert user_model.password == "pass"

    user_model = get_user_by_username("sample1")
    assert user_model.username == "sample1"
    assert user_model.password == "pass1"

    user_model = get_user_by_username("sample2")
    assert user_model.username == "sample2"
    assert user_model.password == "pass2"


def test_get_user_details_by_id(mocker):
    user_details_by_id = {"documentId": "userId", "data": {"username": "sample", "password": "pass"}}
    mocker.patch('src.repository.user_repository.get_user_by_id', return_value=user_details_by_id)
    user_by_id = get_user_details_by_id("userId")
    assert user_by_id["data"] == "sample"


def all_user_data():
    return \
        {
            "data": {
                "userId": {
                    "username": "sample", "password": "pass"
                },
                "userId1": {
                    "username": "sample1", "password": "pass1"
                },
                "userId2": {
                    "username": "sample2", "password": "pass2"
                }
            }
        }