from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from src.model import book


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class BookByIdResponse:
    document_id: str
    data: book

    def __init__(self, document_id, data):
        self.data = data
        self.document_id = document_id


def get_book_data_from_dict(book_json):
    return BookByIdResponse.from_dict(book_json)