import json

from models import Graph


class Converter():
    def decode(self, *args, **kwargs):
        raise NotImplementedError

    def encode(self, *args, **kwargs):
        raise NotImplementedError


class JSONConverter(Converter):

    def encode(self, graph, *args, **kwargs):
        if not isinstance(graph, Graph):
            raise AssertionError

        encoded_graph = {'nodes': [],
                         'edges': [],
                         'attributes': graph.attributes}

        for node in graph.nodes:
            encoded_graph['nodes'].append({'data': {**{'id': node.label}, **node.attributes}})

        for edge in graph.edges:
            encoded_graph['edges'].append({'data': {**{'id': edge.source.label+'_'+edge.target.label,
                                                       'source':edge.source.label,
                                                       'target':edge.target.label}, **edge.attributes}})

        return json.dumps(encoded_graph)
