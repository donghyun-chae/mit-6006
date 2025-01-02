from itertools import permutations
import time

def is_sorted(numbers):
  for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
      return False
  return True

def permutation_sort(A):
  for B in permutations(A):
    if is_sorted(B):
      return B

start_time = time.time()
print(permutation_sort([8,2,4,9,3,1,7,5,6,0]))
end_time = time.time()

print("Time taken :", end_time - start_time)