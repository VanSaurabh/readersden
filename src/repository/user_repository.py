import uuid

from astrapy.rest import http_methods

from src.util import util


def add_user_to_db(user_data):
    collection_name = "user_repo"
    doc_uuid = uuid.uuid4()
    client = util.connect_to_db()

    client.request(
        http_methods.PUT,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}/{doc_uuid}",
        json_data=user_data
    )


def get_all_users_from_db():
    collection_name = "user_repo"
    client = util.connect_to_db()
    return client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}"
    )


def get_user_by_id(user_id):
    collection_name = "user_repo"
    client = util.connect_to_db()
    return client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}/{user_id}"
    )