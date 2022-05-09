from flask import Flask
from src.controller import books_controller

app = Flask(__name__)

# test-endpoint
app.add_url_rule('/rocky', view_func=books_controller.hello_world, methods=['GET'])

# books-endpoints
app.add_url_rule('/books', view_func=books_controller.get_all_books, methods=['GET'])
app.add_url_rule('/books/<book_id>', view_func=books_controller.get_book_by_id, methods=['GET'])
app.add_url_rule('/books', view_func=books_controller.add_books, methods=['POST'])


if __name__ == '__main__':
    app.run()
