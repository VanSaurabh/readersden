from astrapy.rest import AstraClient

from src.util.util import read_config, get_client, connect_to_db


def test_read_config():
    data = read_config('tests/configtest.yaml')
    assert data["cassandra"]["db_id"] == "sample_id"
    assert data["cassandra"]["region"] == "sample_region"
    assert data["cassandra"]["token"] == "sample_token"
    assert data["cassandra"]["keyspace"] == "sample_keyspace"


def test_get_client(mocker):
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = get_client("sample-astra-db-id", "sample-astra-db-region", "sample-astra-db-token")
    assert client is not None
    assert isinstance(client, AstraClient)
    assert client.astra_database_id == "sample-astra-db-id"
    assert client.astra_database_region == "sample-astra-db-region"
    assert client.astra_application_token == "sample-astra-db-token"


def test_connect_to_db(mocker):
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
    mocker.patch('astrapy.rest.create_client', return_value=AstraClient())
    client = connect_to_db()
    assert isinstance(client, AstraClient)
