from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class Book:
    author: str
    book_name: str
    genre: str

    def __init__(self, author, book_name, genre):
        self.book_name = book_name
        self.genre = genre
        self.author = author


def get_book_data_from_dict(data):
    return Book.from_dict(data)


def get_book_data_from_json(data):
    return Book.from_json(data)
