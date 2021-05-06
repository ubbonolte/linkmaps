from flask import jsonify, abort
from converters import JSONConverter
from graph_service import WikiGraphGenerator

class API():

    def read_all(self, *args, **kwargs):
        raise NotImplementedError

    def read(self, *args, **kwargs):
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError

class Wiki(API):


    def __init__(self, service=WikiGraphGenerator()):
        self.service = service

    def read(self, article_uid):
        if len(article_uid) <= 0 or type(article_uid) != str:
            abort(404)

        graph = self.service.generate(article_uid)
        encoded_graph = JSONConverter().encode(graph)
        return jsonify(encoded_graph)