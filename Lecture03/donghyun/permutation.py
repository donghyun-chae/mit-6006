from itertools import permutations

def is_sorted(B):
    for i in range(len(B)-1):
        if B[i] > B[i+1]:
            return False
    return True


def permutation_sort(A):
    '''Sort A'''
    for B in permutations(A):
        if is_sorted(B):
            return B

import time

start_time = time.time()
result = permutation_sort([8,2,4,9,3,1,7,5,6,0])
end_time = time.time()
print(result)
print("Time taken sort:", end_time - start_time)