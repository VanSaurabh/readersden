from flask import Flask, request
from src.service import books_service

app = Flask(__name__)


@app.route('/rocky')
def hello_world():
    """
        a sample endpoint to test flask
    """
    return 'The world is my territory !!', 200, {'Content-Type': 'application/json'}


@app.route('/books', methods=['GET'])
def get_all_books():
    """
        the endpoint returns all the books from db
    """

    return books_service.get_all_books(), 200, {'Content-Type': 'application/json'}


@app.route('/books/<book_id>', methods=['GET'])
def get_book_by_id(book_id):
    """
        the endpoint returns book details by id
    """
    return books_service.get_book_by_id(book_id), 200, {'Content-Type': 'application/json'}


@app.route('/books', methods=['POST'])
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


if __name__ == '__main__':
    app.run()
