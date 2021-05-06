from .mock_db import nodes, edges

class MockWiki():
    def get_nodes(self, node_uids):
        node_list = []

        for node in nodes:
            if node.label in node_uids:
                node_list.append(node)

        return set(node_list)


    def get_edges(self, node_uid):
        edge_list = []

        for edge in edges:
            print(edge.source.label)
            if edge.source.label == node_uid:
                edge_list.append(edge)

        return set(edge_list)