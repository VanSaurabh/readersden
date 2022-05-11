from flask import request

from src.service import books_service
from src.service.login_service import token_verifier


@token_verifier
def hello_world():
    """
        a sample endpoint to test flask
    """
    return 'The world is my territory !!', 200, {'Content-Type': 'application/json'}


@token_verifier
def get_all_books():
    """
        the endpoint returns all the books from db
    """

    return books_service.get_all_books(), 200, {'Content-Type': 'application/json'}


@token_verifier
def get_book_by_id(book_id):
    """
        the endpoint returns book details by id
    """
    return books_service.get_book_by_id(book_id), 200, {'Content-Type': 'application/json'}


@token_verifier
def add_books():
    """
        the endpoint adds a book to the database
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        books_service.add_book(request.json)
        return "Book is saved !", 200, {'Content-Type': 'application/json'}
    else:
        raise 'Content type not supported !'
