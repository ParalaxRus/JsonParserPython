from json_parser.token import JsonToken, JsonTokenType


class JsonTokenizer:

    def __init__(self, val: str):
        self._val = val
        self._pos = 0

    @staticmethod
    def _is_number(c: str) -> bool:
        return (c == '-') or c.isdigit()
    
    @staticmethod
    def _is_alnum(c: str) -> bool:
        return c.isalnum()

    def _skip(self) -> None:
        while self._pos < len(self._val):
            if (self._val[self._pos] != " ") or (self._val[self._pos] != "\t") or (self._val[self._pos] != "\n"):
                break
            self._pos += 1

    def _peek(self) -> str:
        return self._val[self._pos]

    def _get(self) -> str:
        v = self._val[self._pos]
        self._pos += 1
        return v
    
    def _parse_str(self) -> JsonToken:
        val = ''
        while True: 
            c = self._get()
            if c == '"':
                break
            val += c
        return JsonToken(JsonTokenType.STRING, val)
    
    def _parse_str(self) -> JsonToken:
        val = ''
        if self._peek() == '-':
            val = '-'
            self._get()
        while True: 
            c = self._get()
            if not c.isdigit():
                break
            val += c
        return JsonToken(JsonTokenType.NUMBER, val)
    
    def _parse_keyword(self) -> JsonToken:
        val = ''
        while JsonTokenizer._is_alnum(val):
            val += self._get()
        val = val.lower()
        if val == 'true':
            return JsonToken(JsonTokenType.TRUE)
        if val == 'false':
            return JsonToken(JsonTokenType.FALSE)
        if val == 'null':
            return JsonToken(JsonTokenType.NULL)
        return JsonToken(JsonTokenType.UNKNOWN)
    

    def _get_next_token(self) -> JsonTokenType:
        self._skip()
        c = self._peek()

        match c:
            case '{':
                self._get()
                return JsonToken(JsonTokenType.LEFT_BRACE)
            case '}':
                self._get()
                return JsonToken(JsonTokenType.RIGHT_BRACE)
            case '[':
                self._get()
                return JsonToken(JsonTokenType.LEFT_BRACKET)
            case ']':
                self._get()
                return JsonToken(JsonTokenType.RIGHT_BRACKET)
            case ':':
                self._get()
                return JsonToken(JsonTokenType.COLON)
            case ',':
                self._get()
                return JsonToken(JsonTokenType.COMMA)
            case '"':
                self._get()
                return self._parse_str()
            case JsonTokenizer._is_number(c):
                return self._parse_num()
            case JsonTokenizer._is_alnum(c):
                return self._parse_keyword()
            case '\0':
                return JsonToken(JsonTokenType.JSON_END)

    def tokenize(self) -> list['JsonToken']:
        tokens = []
        while True:
            token = self._get_next_token()
            if token.type == JsonTokenType.JSON_END:
                break
            tokens.append(token)
        return tokens
