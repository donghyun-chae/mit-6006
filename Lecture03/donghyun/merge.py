def merge_sort(A, a=0, b=None):
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)
    return A

def merge(L, R, A, i, j, a, b):
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i = i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j -1
        merge(L, R, A, i, j, a, b - 1)

import time
start_time = time.time()
result = merge_sort([8,2,4,9,3,1,7,5,6,0])
end_time = time.time()
print(result)
print("Time taken sort:", end_time - start_time)