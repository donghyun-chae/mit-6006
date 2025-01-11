def merge(A, B):
    i, j = 0, 0
    new_array = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            new_array.append(A[i])
            i += 1
        else:
            new_array.append(B[j])
            j += 1
    if len(A) - i > 0:
        for k in range(i, len(A)):
            new_array.append(A[k])
    if len(B) - j > 0:
        for k in range(j, len(B)):
            new_array.append(B[k])
    return new_array


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        A =  merge(left, right)
    return A

print(merge_sort([2,1,3,5,4,8,6,9,7,0]))