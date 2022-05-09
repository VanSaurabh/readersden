from dataclasses_json import dataclass_json, LetterCase
from dataclasses import dataclass


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserDetails:
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserId:
    userId: UserDetails

    def __init__(self, data):
        self.userId = data


@dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
class UserList:
    data: UserDetails

    def __init__(self, data):
        self.data = data


def get_user_response_from_dict(data):
    return UserList.from_dict(data)
