import json
import uuid

from astrapy.rest import http_methods

from src.model import book, book_by_id_response
from src.util import util


def get_book_by_id(book_id):
    collection_name = "demo_book"
    client = util.connect_to_db()
    book_json = client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}/{book_id}",
    )
    book_by_id = book_by_id_response.get_book_data_from_dict(book_json)
    response = book.get_book_data_from_dict(book_by_id.data)
    return json.dumps(response.__dict__)


def get_all_book_from_db():
    collection_name = "demo_book"
    client = util.connect_to_db()
    return client.request(
        http_methods.GET,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}"
    )


def save_book(book_data):
    collection_name = "demo_book"
    doc_uuid = uuid.uuid4()
    client = util.connect_to_db()

    client.request(
        http_methods.PUT,
        path=f"/api/rest/v2/namespaces/{util.get_keyspace()}/collections/{collection_name}/{doc_uuid}",
        json_data=book_data
    )