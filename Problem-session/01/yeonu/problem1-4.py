# Jen & Berry's

def reorder_students(L):

  # Input: L | linked list with head L.head and size L.size
  # Output: None |
  # This function should modify list L to reverse its last half.
  # Your solution should NOT instantiate:
  # - any additional linked list nodes
  # - any other non-constant-sized data structures


  # 1. Find the n-th node
  n = len(L) // 2
  a = L.head
  for _ in range(n-1):
    a = a.next
  
  # 2. Reverse the order and relink next pointers of last half
  b = a.next
  x_p, x = a, b
  for _ in range(n):
    x_n = x.next
    x.next = x_p
    x_p, x = x, x_n
  
  # 3. Relink front and back of last half
  c = x_p  # head of the last half
  a.next = c
  b.next = None
  
  return