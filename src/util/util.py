import yaml
from astrapy.rest import create_client

astra_db_keyspace = ''
jwt_config = ''


def startup():
    global jwt_config
    jwt_config = read_config('config.yml')


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
    astra_db_id = get_config()["cassandra"]["db_id"]
    astra_db_region = get_config()["cassandra"]["region"]
    astra_db_application_token = get_config()["cassandra"]["token"]
    global astra_db_keyspace
    astra_db_keyspace = get_config()["cassandra"]["keyspace"]
    return get_client(astra_db_id, astra_db_region, astra_db_application_token)


def get_client(astra_db_id, astra_db_region, astra_db_application_token):
    return create_client(astra_database_id=astra_db_id, astra_database_region=astra_db_region,
                         astra_application_token=astra_db_application_token)


def get_keyspace():
    return astra_db_keyspace


def get_config():
    return jwt_config

