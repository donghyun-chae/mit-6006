def direct_access_sort(A):
    '''배열 A안의 요소는 0~u-1 범위의 정수이고 키가 고유해야함'''
    u = max(A) + 1
    D = [None] * u
    for x in A:
        D[x] = x
    i = 0
    for key in range(u):
        if D[key] is not None:
            A[i] = D[key]
            i += 1

arr = [2,3,4,1,5]

print(arr)
direct_access_sort(arr)
print(arr)