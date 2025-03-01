#!/usr/bin/env python3

# Shortest-Paths Tree
def dfs(s, Adj, parent=None, order=None):
    if parent is None:
        parent = dict()
        for v in Adj:
            parent[v] = None
        parent[s] = s
        order = []

    for v in Adj[s].keys():
         if parent[v] is None:
            parent[v] = s
            dfs(v, Adj, parent, order)
    order.append(s)
    return order

def DAG_relax(s, Adj):
     topo = dfs(s, Adj)[::-1]
     print(topo)
     d = dict()
     for v in topo:
         d[v] = float('inf')
     d[s] = 0

     for u in topo:
         for v in Adj[u]:
             if d[v] > d[u] + Adj[u][v]:
                 d[v] = d[u] + Adj[u][v]

     return d

Adj = {
    'a': {'b': -5, 'e': 7},
    'b': {'c': -1, 'e': 6, 'f': -4},
    'c': {},
    'd': {'c': 5},
    'e': {'f': 3},
    'f': {'c': 8, 'g': 2},
    'g': {'c': 1, 'h': -1},
    'h': {'c': 9, 'd': 4},
}
print(DAG_relax('a', Adj))
