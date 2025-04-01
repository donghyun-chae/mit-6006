graph = {
    'a': {'b': -1, 'c': -5, 'd': 3},
    'b': {'f': -1},
    'c': {'f': 3},
    'd': {'b': 2, 'e': 6},
    'e': {'f': -4},
    'f': {}
}

def bellman_ford(Adj, s):
    V = len(Adj)
    d = {u: float('inf') for u in Adj}
    parent = {u: None for u in Adj}
    d[s] = 0
    parent[s] = s

    for _ in range(V - 1):
        for u in Adj:
            for v in Adj[u]:
                if d[v] > d[u] + Adj[u][v]:
                    d[v] = d[u] + Adj[u][v]
                    parent[v] = u

    for u in Adj:
        for v in Adj[u]:
            if d[v] > d[u] + Adj[u][v]:
                raise Exception('There is a negative weight cycle!')

    return d, parent


dist, par = bellman_ford(graph, 'a')
print("Distances:", dist)
print("Parents:", par)
