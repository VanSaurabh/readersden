import yaml

astra_db_id = ''
astra_db_region = ''
astra_db_application_token = ''
astra_db_keyspace = ''


def read_config():
    with open('config.yml') as f:
        global astra_db_id
        global astra_db_region
        global astra_db_application_token
        global astra_db_keyspace

        db_config = yaml.safe_load(f)
        astra_db_id = db_config["cassandra"]["db_id"]
        astra_db_region = db_config["cassandra"]["region"]
        astra_db_application_token = db_config["cassandra"]["token"]
        astra_db_keyspace = db_config["cassandra"]["keyspace"]


read_config()
