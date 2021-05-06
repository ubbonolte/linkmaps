class Graph:
    def __init__(self, nodes=None, edges=None, attributes=None, *args, **kwargs):
        self.nodes = set() if nodes is None else nodes
        self.edges = set() if edges is None else edges
        self.attributes = {} if attributes is None else attributes

    def __str__(self):
        return "<#Nodes = {} | #Edges = {}>".format(len(self.nodes), len(self.edges))



class Node:
    def __init__(self, label, attributes=None, *args, **kwargs):
        self.label = label
        self.attributes = {} if attributes is None else attributes

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(str(self.label))

    def __str__(self):
        return "({})".format(str(self.label))



class Edge:
    def __init__(self, source, target, attributes=None, *args, **kwargs):
        self.source = source
        self.target = target
        self.attributes = {} if attributes is None else attributes

    def __eq__(self, other):
        return self.source == other.source and self.target == other.target

    def __hash__(self):
        return hash(str(self.source) + str(self.target))

    def __str__(self):
        return "{} --> {}".format(str(self.source), str(self.target))

