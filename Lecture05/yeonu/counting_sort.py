def counting_sort(A):
  u = 1 + max([x.key for x in A])
  D = [[] for _ in range(u)]
  for x in A:
    D[x.key].append(x)
  
  i = 0
  for chain in D:
    for x in chain:
      A[i] = x
      i += 1