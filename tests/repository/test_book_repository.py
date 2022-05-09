from src.repository.books_repository import get_client, save_book, connect_to_db, get_book_by_id, get_all_book_from_db
from astrapy.rest import AstraClient, http_methods
from src.model import book_by_id_response, book
from unittest.mock import Mock


def test_get_client(mocker):
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = get_client("sample-astra-db-id", "sample-astra-db-region", "sample-astra-db-token")
    assert client is not None
    assert isinstance(client, AstraClient)
    assert client.astra_database_id == "sample-astra-db-id"
    assert client.astra_database_region == "sample-astra-db-region"
    assert client.astra_application_token == "sample-astra-db-token"


def test_save_book(mocker):
    client = Mock(AstraClient)
    common_mock(mocker)
    mocker.patch('uuid.uuid4', return_value='12')
    mocker.patch('src.repository.books_repository.connect_to_db', return_value=client)
    book_data = {'author': 'Suzanne Collins1', 'book': 'The Hunger Games1', 'genre': ['fiction']}
    save_book(book_data)
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.PUT,
        path='/api/rest/v2/namespaces//collections/demo_book/12',
        json_data=book_data)


def test_get_all_book_from_db(mocker):
    client = Mock(AstraClient)
    common_mock(mocker)
    mocker.patch('src.repository.books_repository.connect_to_db', return_value=client)
    get_all_book_from_db()
    assert client.request.assert_called_once


def test_get_book_by_id(mocker):
    client = Mock(AstraClient)
    sample_book = {
        "document_id": "123",
        "data": {
            "author": "sample",
            "book_name": "sample_book",
            "genre": "test"
        }
    }
    book_data = book.Book('sample', 'sample_book', 'test')
    book_by_id = book_by_id_response.get_book_data_from_dict(sample_book)

    common_mock(mocker)
    mocker.patch('src.repository.books_repository.connect_to_db', return_value=client)
    mocker.patch('src.model.book_by_id_response.get_book_data_from_dict', return_value=book_by_id)
    mocker.patch('src.model.book.get_book_data_from_json', return_value=book_data)
    book_response = get_book_by_id("book_id")
    assert client.request.assert_called_once
    assert book_response == '{"book_name": "sample_book", "genre": "test", "author": "sample"}'


def test_connect_to_db(mocker):
    common_mock(mocker)
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = connect_to_db()
    assert isinstance(client, AstraClient)


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
