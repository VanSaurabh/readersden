from astrapy.rest import create_client, http_methods
from util import astra_db_id, astra_db_keyspace, astra_db_region, astra_db_application_token
import uuid


def main():
    client = get_client()
    add_data_to_db(client)
    delete_data_from_db(client)


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


def delete_data_from_db(client):
    collection_name = "demo_book"
    client.request(http_methods.DELETE, path=f"/api/rest/v2/namespaces/{astra_db_keyspace}/collections/{collection_name}/{id}")


def get_client():
    return create_client(astra_database_id=astra_db_id, astra_database_region=astra_db_region,
                         astra_application_token=astra_db_application_token)


if __name__ == "__main__":
    main()
