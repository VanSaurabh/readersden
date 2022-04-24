from src.main import get_client, connect_to_db, add_data_to_db
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


def test_connect_to_db(mocker):
    mocker.patch('src.util.read_config', return_value={
        'cassandra':
            {'db_id': 'sample_id',
             'region': 'region',
             'token': 'token',
             'keyspace': 'keyspace'
             }
    })
    client = Mock(AstraClient)
    mocker.patch('src.main.get_client', return_value=client)
    mocker.patch('uuid.uuid4', return_value='11')
    connect_to_db()
    client.request.assert_called_once()
    client.request.assert_called_once_with(
        http_methods.PUT,
        path='/api/rest/v2/namespaces/keyspace/collections/demo_book/11',
        json_data={'author': 'Suzanne Collins1', 'book': 'The Hunger Games1', 'genre': ['fiction']})