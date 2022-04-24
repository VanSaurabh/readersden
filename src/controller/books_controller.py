import logging
import jsonpickle
from flask import Flask, Response, request
from src.service import books_service

app = Flask(__name__)


@app.route('/rocky')
def hello_world():
    """
        a sample endpoint to test flask
    """
    return 'The world is my territory !!'


@app.route('/books', methods=['GET'])
def get_all_books():
    """
        the endpoint returns all the books from db
    """
    return books_service.get_all_books()


@app.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    """
        the endpoint returns book details by id
    """
    return books_service.get_book_by_id(book_id)


if __name__ == '__main__':
    app.run()