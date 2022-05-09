from src.util.util import read_config


def test_read_config():
    data = read_config('tests/configtest.yaml')
    assert data["cassandra"]["db_id"] == "sample_id"
    assert data["cassandra"]["region"] == "sample_region"
    assert data["cassandra"]["token"] == "sample_token"
    assert data["cassandra"]["keyspace"] == "sample_keyspace"
