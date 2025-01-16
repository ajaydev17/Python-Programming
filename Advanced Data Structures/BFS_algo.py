"""
Breadth-first search (BFS) explores a graph level by level, starting from a source
node and visiting all of its neighbors before moving on to their neighbors. BFS is useful for
finding the shortest path in unweighted graphs.
"""

from collections import deque

def breadth_first_search(graph, start, end=None):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == end:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Graph represented as an adjacency list
my_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Perform BFS starting from vertex 'A'
breadth_first_search(my_graph, 'A')