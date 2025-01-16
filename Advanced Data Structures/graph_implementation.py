class Graph:

    def __init__(self):
        # dictionary to store adjacency list
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        # add a vertex to the graph
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # add an edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        # remove an edge between two vertices
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        # remove a vertex and all its edges
        if vertex in self.adjacency_list:
            for neighbour in self.adjacency_list[vertex]:
                self.adjacency_list[neighbour].remove(vertex)
            del self.adjacency_list[vertex]

    def display(self):
        # display the adjacency list
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")