import jwt
from werkzeug.security import generate_password_hash

from src.main import app
from src.model.user_model import UserModel
from src.service.login_service import login_by_username_password, token_verifier


def test_login_by_username_password_success(mocker):
    sample_password_hash = generate_password_hash(password='pass')
    with app.test_request_context('/login', data={'username': 'sample', 'password': 'pass'}):
        mocker.patch('src.service.user_service.get_user_by_username',
                     return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.get_config',
                     return_value={'jwt': {'token': {'secret': 'sample-token', 'expiration': 5}}})
        actual_result = login_by_username_password()
        assert jwt.decode(actual_result, options={"verify_signature": False})["userId"] == 'sample'
        assert actual_result is not None


def test_login_by_username_password_fail_when_password_dont_match(mocker):
    sample_password_hash = generate_password_hash(password='pass1')
    with app.test_request_context('/login', data={'username': 'sample', 'password': 'pass'}):
        mocker.patch('src.service.user_service.get_user_by_username',
                     return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.get_config',
                     return_value={'jwt': {'token': {'secret': 'sample-token', 'expiration': 5}}})
        actual_result = login_by_username_password()
        assert actual_result is None


def test_login_by_username_password_fail_when_auth_is_not_present(mocker):
    sample_password_hash = generate_password_hash(password='pass')
    with app.test_request_context('/login', data={'test': 'test'}):
        mocker.patch('src.service.user_service.get_user_by_username',
                     return_value=UserModel('sample', sample_password_hash))
        mocker.patch('src.util.util.get_config',
                     return_value={'jwt': {'token': {'secret': 'sample-token', 'expiration': 5}}})
        actual_result = login_by_username_password()
        assert actual_result is None


def test_token_verifier_success(mocker):
    with app.test_request_context('/login', headers={'X-Access-Token': 'testToken'}):
        mocker.patch('src.util.util.get_config',
                     return_value={'jwt': {'token': {'secret': 'sample-token', 'expiration': 5}}})
        mocker.patch('jwt.decode', return_value={'userId': 'sample'})
        mocker.patch('src.service.user_service.get_user_by_username', return_value=UserModel)
        verify_jwt = token_verifier(functest)
        result = verify_jwt()
        assert result is None


def test_token_verifier_when_user_is_invalid(mocker):
    with app.test_request_context('/login', headers={'X-Access-Token': 'testToken'}):
        mocker.patch('src.util.util.get_config',
                     return_value={'jwt': {'token': {'secret': 'sample-token', 'expiration': 5}}})
        mocker.patch('jwt.decode', return_value={'userId': 'sample'})
        mocker.patch('src.service.user_service.get_user_by_username', return_value=None)
        verify_jwt = token_verifier(functest)
        result = verify_jwt()
        assert result == ({'error': 'Invalid token !'}, 401, {'Content-Type': 'application/json'})


def test_token_verifier_when_token_is_not_present():
    with app.test_request_context('/login', headers={'token': 'testToken'}):
        verify_jwt = token_verifier(functest)
        result = verify_jwt()
        assert result == ({'error': 'Token is required !'}, 401, {'Content-Type': 'application/json'})


def functest():
    pass
