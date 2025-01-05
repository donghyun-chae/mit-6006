def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j - 1], A[j] = A[j], A[j - 1] 
            j -= 1
    return A
print(insertion_sort([2,3,5,4,1]))