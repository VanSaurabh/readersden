from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from src.model import user_model


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserDetailsById:
    document_id: str
    data: user_model.UserModel

    def __init__(self, document_id, data):
        self.data = data
        self.document_id = document_id


def get_user_details_by_id_from_dict(book_json):
    return UserDetailsById.from_dict(book_json)
