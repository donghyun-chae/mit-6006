graph = [[],[2],[3],[4,5,6],[7],[7],[8],[8],[1],[10],[],[12],[13],[14,15],[16],[16],[]]

def bfs(s, parent, Adj):
  level = [[s]]
  parent[s] = s
  while len(level[-1]) > 0:
    level.append([])
    for u in level[-2] :
      for v in Adj[u] :
        if parent[v] == None :
          parent[v] = u
          level[-1].append(v)
  return parent

def full_bfs(Adj):
  parent = [None for _ in graph]
  for v in range(len(graph)):
    if parent[v] is None:
      bfs(v, parent, Adj)
  return parent

print(full_bfs(graph))


# t = int(input())
# path = [t]

# while parent[t] != None and t != s:
#   path.append(parent[t])
#   t = parent[t]

# if t == s:
#   print(path[::-1])
# else:
#   print("fail")