from src.repository.books_repository import get_client, connect_to_db, add_data_to_db, get_book_by_id, get_all_book_from_db
from astrapy.rest import AstraClient, http_methods
from unittest.mock import Mock


def test_get_client(mocker):
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = get_client("sample-astra-db-id", "sample-astra-db-region", "sample-astra-db-token")
    assert client is not None
    assert isinstance(client, AstraClient)
    assert client.astra_database_id == "sample-astra-db-id"
    assert client.astra_database_region == "sample-astra-db-region"
    assert client.astra_application_token == "sample-astra-db-token"


def test_add_data_to_db(mocker):
    client = Mock(AstraClient)
    mocker.patch('uuid.uuid4', return_value='12')
    add_data_to_db(client)
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.PUT,
        path='/api/rest/v2/namespaces//collections/demo_book/12',
        json_data={'author': 'Suzanne Collins1', 'book': 'The Hunger Games1', 'genre': ['fiction']})


def test_get_all_book_from_db(mocker):
    client = Mock(AstraClient)
    mocker.patch('src.util.read_config',
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
    mocker.patch('src.repository.books_repository.connect_to_db', return_value=client)
    get_all_book_from_db()
    assert client.request.assert_called_once


def test_get_book_by_id(mocker):
    client = Mock(AstraClient)
    mocker.patch('src.util.read_config',
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
    mocker.patch('src.repository.books_repository.connect_to_db', return_value=client)
    get_book_by_id("book_id")
    assert client.request.assert_called_once


def test_connect_to_db(mocker):
    mocker.patch('src.util.read_config',
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
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = connect_to_db()
    assert isinstance(client, AstraClient)
