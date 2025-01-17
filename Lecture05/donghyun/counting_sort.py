def counting_sort(A):
    u = max(A) + 1
    D = [0] * u
    for x in A:
        D[x] += 1
    
    for k in range(1, u):
        D[k] += D[k - 1]
    
    for x in list(reversed(A)):
        A[D[x] - 1] = x
        D[x] -= 1

arr = [4,1,1,3]

print(arr)
counting_sort(arr)
print(arr)
