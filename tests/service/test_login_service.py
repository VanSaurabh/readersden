from src.main import app
from src.model.user_model import UserModel
from src.service.login_service import login_by_username_password
from werkzeug.security import generate_password_hash
import jwt


def test_login_by_username_password_success(mocker):
    sample_password_hash = generate_password_hash(password='pass')
    with app.test_request_context('/login', data={'username': 'sample', 'password': 'pass'}):
        mocker.patch('src.service.user_service.get_user_by_username', return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.read_config', return_value={'jwt': {'token': {'secret': 'sample-token'}}})
        actual_result = login_by_username_password()
        assert jwt.decode(actual_result, options={"verify_signature": False})["userId"] == 'sample'
        assert actual_result is not None


def test_login_by_username_password_fail_when_password_dont_match(mocker):
    sample_password_hash = generate_password_hash(password='pass1')
    with app.test_request_context('/login', data={'username': 'sample', 'password': 'pass'}):
        mocker.patch('src.service.user_service.get_user_by_username', return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.read_config', return_value={'jwt': {'token': {'secret': 'sample-token'}}})
        actual_result = login_by_username_password()
        assert actual_result is None


def test_login_by_username_password_fail_when_auth_is_not_present(mocker):
    sample_password_hash = generate_password_hash(password='pass')
    with app.test_request_context('/login', data={'test': 'test'}):
        mocker.patch('src.service.user_service.get_user_by_username', return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.read_config', return_value={'jwt': {'token': {'secret': 'sample-token'}}})
        actual_result = login_by_username_password()
        assert actual_result is None

