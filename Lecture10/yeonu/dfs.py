def dfs(s, parent, order):

  for v in adj[s]:
    if parent[v] == None:
      parent[v] = s
      dfs(v, parent, order)
  order.append(s)

def full_dfs(adj):
  parent = [None for _ in range(len(adj))]
  order = []
  for s in range(1, len(adj)):
    if parent[s] == None:
      parent[s] = s
      dfs(s, parent, order)

  print("parent: ", parent)
  print("order: ", order)

adj = [[],[3,5],[],[4,5],[],[4,6],[3]]
full_dfs(adj)

# 1->3->4->5->6-> 2