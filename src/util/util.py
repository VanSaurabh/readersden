import yaml
from astrapy.rest import create_client

astra_db_keyspace = ''


def read_config(file):
    try:
        with open(file) as f:
            try:
                return yaml.safe_load(f)
            except ValueError:
                raise ValueError('config.yml is invalid !')
    except IOError:
        raise IOError('got error while opening config.yml file !')


def connect_to_db():
    db_config = read_config('config.yml')
    astra_db_id = db_config["cassandra"]["db_id"]
    astra_db_region = db_config["cassandra"]["region"]
    astra_db_application_token = db_config["cassandra"]["token"]
    global astra_db_keyspace
    astra_db_keyspace = db_config["cassandra"]["keyspace"]
    return get_client(astra_db_id, astra_db_region, astra_db_application_token)


def get_client(astra_db_id, astra_db_region, astra_db_application_token):
    return create_client(astra_database_id=astra_db_id, astra_database_region=astra_db_region,
                         astra_application_token=astra_db_application_token)


def get_keyspace():
    return astra_db_keyspace
