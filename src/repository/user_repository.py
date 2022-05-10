from astrapy.rest import create_client, http_methods
import src.util.util
import uuid


astra_db_keyspace = ''


def connect_to_db():
    db_config = src.util.util.read_config('config.yml')
    astra_db_id = db_config["cassandra"]["db_id"]
    astra_db_region = db_config["cassandra"]["region"]
    astra_db_application_token = db_config["cassandra"]["token"]
    global astra_db_keyspace
    astra_db_keyspace = db_config["cassandra"]["keyspace"]
    return get_client(astra_db_id, astra_db_region, astra_db_application_token)


def add_user_to_db(user_data):
    collection_name = "user_repo"
    doc_uuid = uuid.uuid4()
    client = connect_to_db()

    client.request(
        http_methods.PUT,
        path=f"/api/rest/v2/namespaces/{astra_db_keyspace}/collections/{collection_name}/{doc_uuid}",
        json_data=user_data
    )


def get_all_users_from_db():
    collection_name = "user_repo"
    client = connect_to_db()
    return client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{astra_db_keyspace}/collections/{collection_name}"
    )


def get_user_by_id(user_id):
    collection_name = "user_repo"
    client = connect_to_db()
    return client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{astra_db_keyspace}/collections/{collection_name}/{user_id}"
    )


def get_client(astra_db_id, astra_db_region, astra_db_application_token):
    return create_client(astra_database_id=astra_db_id, astra_database_region=astra_db_region,
                         astra_application_token=astra_db_application_token)