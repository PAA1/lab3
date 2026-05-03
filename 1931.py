import heapq

def dijkstra(graph, source: str):
    dist = {node: float('inf') for node in graph}

    return dist


n, m = (int(x) for x in input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, w = (int(x) for x in input().split())
    
    # Preencha o grafo


dist = dijkstra(graph, 1)
