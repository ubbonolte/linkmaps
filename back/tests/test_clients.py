from clients import WikiClient
from models import Node


def test_wiki_client():
    w = WikiClient()

    nodes = w.get_nodes(['Albert Einstein'])
    assert len(nodes) == 1

    node = nodes.pop()
    assert node.label == 'Albert Einstein'

    edges = w.get_edges('Albert Einstein')
    assert len(edges) > 10

    edge = edges.pop()
    assert Node("Albert Einstein") == edge.source

