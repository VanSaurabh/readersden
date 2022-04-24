from src.repository import books_repository


def get_all_books():
    return books_repository.get_all_book_from_db()


def get_book_by_id(book_id):
    return books_repository.get_book_by_id(book_id)