#!/usr/bin/env python3
#
n = int(input())
m = int(input())

relation = dict()
result = [0 for _ in range(n+1)]
for _ in range(m):
    t, s, w = map(int, input().split())
    temp = relation.get(s, [])
    temp.append([t, w])
    relation[s] = temp


def dfs(Adj, s, count, parent=None, order=None):
    if parent is None:
        parent = [None for _ in Adj]
        parent[s] = s
        order = []
    if s !=  n:
        for v in Adj[s]:
            if parent[v[0]] is None:
                parent[v[0]] = s
                count = count* dfs(Adj, v[0],  count*v[1], parent, order)
    order.append(s)
    return count

def full_dfs(Adj):
    parent = [None for _ in range(n+1)]
    order = []
    for v in range(1, len(Adj)+1):
        if parent[v] is None:
            parent[v] = v
            count = dfs(Adj, v, 1, parent, order)
            result[v] += count
    return parent, order[::-1]
print(relation)
print(full_dfs(relation))
print(result)
