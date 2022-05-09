from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserModel:
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password


def get_user_model_from_dict(data):
    return UserModel.from_dict(data)


def get_user_model_from_json(data):
    return UserModel.from_json(data)