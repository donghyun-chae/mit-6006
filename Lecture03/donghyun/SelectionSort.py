def selection_sort(A):
    for i in range(len(A) - 1, 0, -1):
        temp = i
        for j in range(i):
            if A[temp] < A[j]:
                temp = j
        A[temp], A[i] = A[i], A[temp]
    return A

print(selection_sort([2,1,4,5,3]))
