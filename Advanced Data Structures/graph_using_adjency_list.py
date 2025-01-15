"""
: A graph can be implemented using a dictionary where each key is a node, and the
value is a list of neighboring nodes. This approach allows efficient storage and traversal of
sparse graphs.
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[v].append(u) # for undirected graphs