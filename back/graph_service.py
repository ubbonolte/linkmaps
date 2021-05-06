from clients import WikiClient
from models import Graph

class GraphService:
    def generate(self, *args, **kwargs):
        raise NotImplementedError

class WikiGraphGenerator(GraphService):

    def __init__(self, client=None, wiki_language='en'):
        self.client= WikiClient() if client is None else client
        self.client.language = wiki_language

    def generate(self, root_title, depth=2, max_visits = 100, *args, **kwargs):
        graph = Graph()
        graph.attributes['depth'] = depth
        graph.attributes['complete'] = True
        titles = set()
        titles.add(root_title)
        visited = set()

        while depth > 0:
            depth -= 1
            to_visit = titles - visited

            while to_visit:
                title = to_visit.pop()
                visited.add(title)

                graph.edges = graph.edges.union(self.client.get_edges(title))

                for edge in graph.edges:
                    graph.nodes.add(edge.source)
                    titles.add(edge.source.label)

                    graph.nodes.add(edge.target)
                    titles.add(edge.target.label)

                if len(visited) > max_visits:
                    graph.attributes['complete'] = False if len(titles) > max_visits else True
                    return graph

        return graph







