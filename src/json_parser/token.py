from enum import Enum
from typing import Self

class JsonTokenType(Enum):
        LEFT_BRACE = 1 # {
        RIGHT_BRACE = 2 # }
        LEFT_BRAKET = 3 # [
        RIGHT_BRAKET = 4 # ]
        COLON = 5 # :
        COMMA = 6 # ,
        STRING = 7
        NUMBER = 8
        TRUE = 9
        FALSE = 10
        NULL = 11
        JSON_END = 12
        UNKNOWN = 13

class JsonToken:
    def __init__(self, type: JsonTokenType, value: str = '') -> Self:
        self.type = type
        self.value = value
