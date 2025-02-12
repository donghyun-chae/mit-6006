def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    ##################
    longest = 1
    current = 1
    for i in range(1, len(A)):
        if A[i-1] < A[i]:
            current += 1

        else:
            if current == longest:
                count +=1
            elif current > longest:
                longest = current
                count = 1
            current = 1
    if current > longest:
        longest = current
        count = 1
    elif current == longest:
        count += 1

    # ##################
    return count
