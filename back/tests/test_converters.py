from converters import JSONConverter
from . import mock_db


def test_json_converter():

    """Test Empty-Graph"""
    g = mock_db.graph_empty

    converter = JSONConverter()
    encoded_g = converter.encode(g)

    assert encoded_g == '{"nodes": [], "edges": [], "attributes": {}}'

    """Test A-B-Graph"""
    g = mock_db.graph_a_b

    converter = JSONConverter()
    encoded_g = converter.encode(g)

    print(type(encoded_g), encoded_g)

    assert '{"data": {"id": "node_a", "a": 1}}' in encoded_g
    assert '[{"data": {"id": "node_a_node_b", "source": "node_a", "target": "node_b", "a": 1}}]' in encoded_g
