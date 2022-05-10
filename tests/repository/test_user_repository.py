from unittest.mock import Mock

from astrapy.rest import AstraClient, http_methods

from src.repository.user_repository import add_user_to_db, get_user_by_id, get_all_users_from_db


def test_add_user_to_db(mocker):
    client = Mock(AstraClient)
    common_mock(mocker)
    mocker.patch('uuid.uuid4', return_value='12')
    mocker.patch('src.util.util.connect_to_db', return_value=client)
    user_data = {'username': 'sample', 'password': 'pass'}
    add_user_to_db(user_data)
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.PUT,
        path='/api/rest/v2/namespaces//collections/user_repo/12',
        json_data=user_data)


def test_get_all_users_from_db(mocker):
    client = Mock(AstraClient)
    common_mock(mocker)
    mocker.patch('src.util.util.connect_to_db', return_value=client)
    get_all_users_from_db()
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.GET,
        path='/api/rest/v2/namespaces//collections/user_repo'
    )


def test_get_user_by_id(mocker):
    client = Mock(AstraClient)
    common_mock(mocker)
    mocker.patch('src.util.util.connect_to_db', return_value=client)
    get_user_by_id("userId")
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.GET,
        path='/api/rest/v2/namespaces//collections/user_repo/userId'
    )


def common_mock(mocker):
    mocker.patch('src.util.util.read_config',
                 return_value=
                 {
                     "cassandra":
                         {
                             "db_id": "id",
                             "region": "region",
                             "token": "token",
                             "keyspace": "keyspace"
                         }
                 })