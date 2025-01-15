import counting_sort

def radix_sort(A):
  n = len(A)
  u = 1 + max([x.key for x in A])
  c = 1 + (u.bit_length() // n.bit_length)

  class Obj: pass
  D = [Obj() for a in A]
  for i in range(n):
    D[i].digits = []
    D[i].item = A[i]
    high = A[i].key
    for j in range(c):
      high, low = divmod(high, n)
      D[i].digits.append(low)
  for i in range(c):
    for j in range(n):
      D[j].key = D[j].digits[i]
    counting_sort(D)
  for i in range(n):
    A[i] = D[i].item
