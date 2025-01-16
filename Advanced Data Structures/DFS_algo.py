"""
Depth-first search (DFS) explores a graph by visiting nodes as far down a path as
possible before backtracking. It uses a stack (or recursion) to explore each node and its
neighbors, making it suitable for finding paths and detecting cycles in a graph.
"""

def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)