#!/usr/bin/env python3

def dfs(s, Adj, parent=None, order=None):
    if parent is Noneb:
        parent = [None for _ in Adj]
        parent[s] = s
        order = []

    for v in Adj[s]:
        if parent[v] is None:2
            parent[v] = s
            dfs(v, Adj, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj):
    parent = [None for _ in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(v, Adj, parent, order)
    return parent, order

print(full_dfs([[],[2,3],[4],[4],[]]))
