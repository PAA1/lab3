import heapq


# Você precisa modificar o algoritmo de dijkstra abaixo para resolver o problema!
def dijkstra(graph, source):
    """
    Dijkstra O((|E| + |V|) log |V|) com heap binário.

    Parâmetros:
      graph: dicionário (lista de adjacência) representando grafo valorado com arestas não-negativas.
      source: nó de origem.

    Retorna:
      dist: dicionário com a menor distância da origem para cada nó.
            Para nós inalcançáveis, distância = float('inf').
      parent: dicionário com o predecessor imediato no caminho mínimo
              (None para a origem e para nós inalcançáveis).
    """

    # Inicialização
    processado = set()
    dist = {v: float('inf') for v in graph.keys()}
    parent = {v: None for v in graph.keys()}

    dist[source] = 0  # Origem começa com distância zero

    fila = [(0.0, source)]

    while fila:  # enquanto fila não for vazia
        du, u = heapq.heappop(fila)  # extrai nodo com menor distância na fila
    
        if u in processado:
            continue
        processado.add(u)

        for v, wv in graph[u]:    # para cada vizinho v de u
            novo_dv = du + wv     # distância até u mais peso da aresta u-v
            if novo_dv < dist[v]: # se distância menor que a atual
                dist[v] = novo_dv
                parent[v] = u
                heapq.heappush(fila, (novo_dv, v))  # coloca v na fila com sua distância atual da origem

    return dist, parent


n, m = (int(x) for x in input().split())
graph = {i : [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, w = (int(x) for x in input().split())
    
    # Preencha o grafo


dist = dijkstra(graph, 1)

# Imprima a resposta
