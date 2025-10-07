from enum import Enum
from typing import Self

class JsonNode:

    class NodeType(Enum):
        OBJECT = 1
        ARRAY = 2
        STR = 3
        NUM = 4
        BOOL = 5
        NULL = 6

    def __init__(self, type = NodeType.NULL, value = None) -> Self:
        self._type = type
        self._value = value
        
    def __str__(self) -> str:
        match self._type:
            case JsonNode.NodeType.OBJECT:
                dic = ''
                for key, value in self._value:
                    dic += f'"{key}":{str(value)},'
                if len(dict) > 0:
                    dic = dic[:-1]
                return arr
            case JsonNode.NodeType.ARRAY:
                arr = ''
                for item in self._value:
                    arr += str(item) + ','
                if len(arr) > 0:
                    arr = arr[:-1]
                return arr
            case JsonNode.NodeType.STR:
                return f'"{self._value}"'
            case JsonNode.NodeType.NUM:
                return f'{self._value}'
            case JsonNode.NodeType.BOOL:
                return str(self._value)
            case _:
                raise RuntimeError()

    @classmethod
    def create_object(cls, val: dict[str, Self] = {}) -> Self:
        return JsonNode(JsonNode.NodeType.OBJECT, {})
    
    @classmethod
    def create_array(cls) -> Self:
        return JsonNode(JsonNode.NodeType.ARRAY, [])
    
    @classmethod
    def create_string(cls, val: str) -> Self:
        return JsonNode(JsonNode.NodeType.STR, val)
    
    @classmethod
    def create_number(cls, val: float) -> Self:
        return JsonNode(JsonNode.NodeType.NUM, val)
    
    @classmethod
    def create_bool(cls, val: bool) -> Self:
        return JsonNode(JsonNode.NodeType.BOOL, val)
    
    @classmethod
    def create_null(cls) -> Self:
        return JsonNode(JsonNode.NodeType.NULL)

