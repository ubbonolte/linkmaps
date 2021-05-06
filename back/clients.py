import re

import requests

from models import Node, Edge


class APIClient():
    def get_nodes(self, node_uids: list, *args: object, **kwargs: object) -> set:
        """
        Takes a list of uids and returns a list of Nodes

        :param node_ids: a list of node_uids
        :param args:
        :param kwargs:
        """
        raise NotImplementedError

    def get_edges(self, node_uid: object, *args: object, **kwargs: object) -> set:
        """
        Takes a node uid and returns adjacent edges

        :param node_uids: a list of node_uids
        :param args:
        :param kwargs:
        """
        raise NotImplementedError


class WikiClient(APIClient):

    def __init__(self, language='en', base_url="https://{}.wikipedia.org/w/api.php", session=requests.Session(),
                 max_retry=10):
        self.language=language
        self.session = session
        self.url = base_url
        self.max_retry = max_retry

    def get_nodes(self, node_uids: list, *args: object, **kwargs: object) -> set:
        """ATM nodes don't contain any other Infos then their label"""
        nodes = set()

        for uid in node_uids:
            if self.is_valid_node(uid):
                nodes.add(Node(label=uid))

        return nodes

    def get_edges(self, node_uid, *args, **kwargs):
        """Wikipedia Edges are links between articles"""
        root_nodes = self.get_nodes([node_uid])
        if root_nodes:
            root = root_nodes.pop()
        else:
            return set()

        links = self.get_links(node_uid)

        edges = set()

        for node in self.get_nodes(links):
            edges.add(Edge(source=root, target=node))

        return edges


    def get_links(self, node_uid):
        """Calls Wikipedia API to get all outlinks of article with node_uid"""
        PARAMS = {
            "action": "query",
            "format": "json",
            "pllimit": "max",
            "prop": "links",
            "titles": node_uid,
            "namespace": 0
        }
        data = []
        continue_ = True

        while continue_:
            """Continue until all links are collected"""
            errors = 0

            result = self.get(PARAMS)  # API-Call

            if result.ok:
                errors = 0

                for _, v in result.json()['query']['pages'].items():
                    if 'links' in v:
                        data += v['links']
                    else:
                        pass
                        # TODO Log unexpected result

                if 'continue' in result.json():
                    PARAMS['plcontinue'] = result.json()['continue']['plcontinue']
                else:
                    continue_ = False
                    PARAMS.pop('plcontine', None)

            else:
                errors += 1
                if errors > self.max_retry:
                    return False

        return [d['title'] for d in data]

    def get(self, params, *args, **kwargs):
        """Returns request object of api-call with params"""
        return self.session.get(url=self.url.format(self.language), params=params)

    def is_valid_node(self, node_label):
        """
        Returns False if node_label starts with 'word:something' else returns True.

        This should identify most of the technical articles like categories or portals.
        """
        if re.match(r'\S+:\S.*', node_label):
            return False
        else:
            return True



