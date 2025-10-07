from json_parser.parser import JsonParser

def test_empty_json():
    parser = JsonParser()
    node = parser.parse('{}')
    assert str(node) == '{}'