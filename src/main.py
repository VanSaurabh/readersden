from astrapy.rest import create_client, http_methods
import src.util
import uuid

astra_db_keyspace = ''


def connect_to_db():
    db_config = src.util.read_config('config.yml')
    astra_db_id = db_config["cassandra"]["db_id"]
    astra_db_region = db_config["cassandra"]["region"]
    astra_db_application_token = db_config["cassandra"]["token"]
    global astra_db_keyspace
    astra_db_keyspace = db_config["cassandra"]["keyspace"]
    client = get_client(astra_db_id, astra_db_region, astra_db_application_token)
    add_data_to_db(client)


def add_data_to_db(client):
    collection_name = "demo_book"
    doc_uuid = uuid.uuid4()

    client.request(
        http_methods.PUT,
        path=f"/api/rest/v2/namespaces/{astra_db_keyspace}/collections/{collection_name}/{doc_uuid}",
        json_data={
            "book": "The Hunger Games1",
            "author": "Suzanne Collins1",
            "genre": ["fiction"],
        }
    )


def get_client(astra_db_id, astra_db_region, astra_db_application_token):
    return create_client(astra_database_id=astra_db_id, astra_database_region=astra_db_region,
                         astra_application_token=astra_db_application_token)


if __name__ == "__main__":
    connect_to_db()
