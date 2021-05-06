from graph_service import WikiGraphGenerator
from . import mock_client


def test_wiki_generator():
    graph_generator = WikiGraphGenerator(client=mock_client.MockWiki())
    graph = graph_generator.generate('node_a')

    assert len(graph.edges) == 2
    assert len(graph.nodes) == 3
