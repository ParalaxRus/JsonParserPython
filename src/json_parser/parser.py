from node import JsonNode
from token import JsonTokenType
from tokenizer import JsonTokenizer

class JsonParser:

    def __init__(self):
        self._idx = 0
        self._tokens = []

    def parse_object(self) -> JsonNode:
        node = JsonNode.create_object()
        while self._tokens[self._idx].type != JsonTokenType.RIGHT_BRACKET:
            self._idx += 1
            next = self._tokens[self._idx]
            if next.type != JsonTokenType.STRING:
                raise RuntimeError()
            key = next.value
            self._idx += 1
            if next.type != JsonTokenType.COLON:
                raise RuntimeError()
            self._idx += 1
            node[key] = self._parse()
        return node


    def parse_list(self) -> JsonNode:
        node = JsonNode.create_list()
        while self._tokens[self._idx].type != JsonTokenType.RIGHT_BRACKET:
            self._idx += 1
            if next.type != JsonTokenType.COMMA:
                continue
            next = self._parse()
            node.appeend(next)
        return node

    def _parse(self) -> JsonNode:
        if self._idx >= len(self._tokens):
            return JsonNode(JsonNode.NodeType.NULL)
        match self._tokens[self._idx].type:
            case JsonTokenType.LEFT_BRACE:
                return self._parse_object()
            case JsonTokenType.LEFT_BRACKET:
                return self._parse_list()
            case JsonTokenType.STRING:
                return JsonNode.create_string(self._tokens[self._idx].value)
            case JsonTokenType.NUMBER:
                return JsonNode.create_number(self._tokens[self._idx].value)
            case JsonTokenType.TRUE:
                return JsonNode.create_bool(True)
            case JsonTokenType.FALSE:
                return JsonNode.create_bool(False)
            case JsonTokenType.NULL:
                return JsonNode.create_null()
        
    def parse(self, val: str) -> JsonNode:
        tokenizer = JsonTokenizer(val)
        self._idx = 0
        self._tokens = tokenizer.tokenize()
        return self._parse()

