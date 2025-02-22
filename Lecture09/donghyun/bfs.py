#!/usr/bin/env python3

def bfs(s, parent, Adj):
    level = [[s]]
    parent[s] = s
    while len(level[-1]) > 0:
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    level[-1].append(v)
                    parent[v] = u

def full_bfs(Adj):
    parent = [None for _ in Adj]
    for v in range(len(Adj)):
        if parent[v] is None:
            bfs(v, parent, Adj)
    return parent

graph = [[],[2,3],[4],[5],[],[]]

print(full_bfs(graph))
