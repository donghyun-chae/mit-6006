def find_max(A, i):
    if i > 0:
        j = find_max(A, i-1)
        if A[i] < A[j]:
            return j
    return i
    
def selection_sort(A, start = None):
    if start == 0:
        return A
    if start is None:
        start = len(A) - 1
    before = A[start]
    largest = find_max(A, start)
    A[start] = A[largest]
    A[largest] = before
    return selection_sort(A, start - 1)


import time
start_time = time.time()
result = selection_sort([8,2,4,9,3,1,7,5,6,0,10,11])
end_time = time.time()
print(result)
print("Time taken sort:", end_time - start_time)


