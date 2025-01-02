import time

def selection_sort(A, start = None):
  if start is None:  
    start = len(A) - 1
  if (start == 0) :
    return
  x = find_max(A, start)
  A[x], A[start] = A[start], A[x]
  selection_sort(A, start-1)

def find_max(A, i):
    if i == 0:  
        return 0
    max_index = find_max(A, i - 1)
    return i if A[i] > A[max_index] else max_index


start_time = time.time()
arr = [8,2,4,9,3,1,7,5,6,0]
selection_sort(arr)
print(arr)
end_time = time.time()

print("Time taken :", end_time - start_time)