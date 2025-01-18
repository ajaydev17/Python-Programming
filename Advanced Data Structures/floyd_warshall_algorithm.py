"""
The Floyd-Warshall algorithm calculates shortest paths between all node pairs in
O(n³) time. It iteratively updates distances using each node as an intermediate step.
"""

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0
        for v, weight in graph[u]:
            dist[u][v] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist