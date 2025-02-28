def dfs(Adj, s, parent, order):

  for v in Adj[s]:
    if parent[v] == None:
      parent[v] = s
      dfs(v, parent, order)
  order.append(s)

  return parent, order

def relax(Adj, w, d, parent, u, v):
  if d[v] > d[u] + w(u,v): 
    d[v] = d[u] + w(u,v)
    parent[v] = u

def DAG_Relaxation(Adj, w, s):
  _, order = dfs(Adj, s)
  order.reverse()
  d = [float('inf') for _ in Adj]
  parent = [None for _ in Adj]
  d[s], parent[s] = 0, s
  for u in order:
    for v in Adj[u]:
      relax(Adj, w, d, parent, u, v)
  return d, parent
