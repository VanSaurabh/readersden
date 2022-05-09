from flask import Flask
from src.controller import books_controller, login_controller, user_controller

app = Flask(__name__)


# test-endpoint
app.add_url_rule('/rocky', view_func=books_controller.hello_world, methods=['GET'])

# books-endpoints
app.add_url_rule('/books', view_func=books_controller.get_all_books, methods=['GET'])
app.add_url_rule('/books/<book_id>', view_func=books_controller.get_book_by_id, methods=['GET'])
app.add_url_rule('/books', view_func=books_controller.add_books, methods=['POST'])

# login-controller
app.add_url_rule('/login', view_func=login_controller.login, methods=['POST'])


# user-controller
app.add_url_rule('/users', view_func=user_controller.add_user, methods=['POST'])
app.add_url_rule('/users', view_func=user_controller.get_all_users, methods=['GET'])
app.add_url_rule('/users/<user_id>', view_func=user_controller.get_user_by_id, methods=['GET'])


if __name__ == '__main__':
    app.run()
