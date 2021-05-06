from models import Graph, Node, Edge
"""Nodes"""
node_a = Node('node_a', {'a':1})
node_b = Node('node_b', {'b':1})
node_c = Node('node_c', {'c':1})

nodes = [node_a, node_b, node_c]

"""Edges"""
edge_a_b = Edge(node_a, node_b, {'a':1})
edge_b_c = Edge(node_b, node_c, {'a':1})

edges = [edge_a_b, edge_b_c]

"""Graphs"""
graph_empty = Graph()

graph_a_b = Graph()
graph_a_b.nodes.add(node_a)
graph_a_b.nodes.add(node_b)

graph_a_b.edges.add(edge_a_b)