from . import mock_db

def test_graph_model():
    g = mock_db.graph_empty
    assert g
    assert g.nodes == set()
    assert g.edges == set()

def test_node():
    n = mock_db.node_a
    assert n
    assert n.label == 'node_a'
    assert n.attributes == {'a':1}

def test_edge():
    n1 = mock_db.node_a
    n2 = mock_db.node_b
    e = mock_db.edge_a_b
    assert e
    assert e.source == n1
    assert e.target == n2
    assert e.attributes == {'a': 1}