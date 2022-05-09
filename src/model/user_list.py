from dataclasses_json import dataclass_json, LetterCase
from dataclasses import dataclass


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserList:
    username: [str]

    def __init__(self, username):
        self.username = username


def get_user_response_from_dict(data):
    return UserList.from_dict(data)
