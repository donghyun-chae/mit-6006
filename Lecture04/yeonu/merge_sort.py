def merge_sort(A):

  if len(A) <= 1:
    return A
  
  mid = len(A)//2
  a = merge_sort(A[:mid])
  b = merge_sort(A[mid:])
  
  return merge(a, b)

def merge(a, b):
  merged_list = []
  i, j = 0, 0
  while(i < len(a) and j < len(b)):
    if a[i] <= b[j]:
      merged_list.append(a[i])
      i += 1
    else:
      merged_list.append(b[j])
      j += 1

  if (i <= len(a) - 1):
    for k in range(i, len(a)):
      merged_list.append(a[k])
  if (j <= len(b) - 1):
    for k in range(j, len(b)):
      merged_list.append(b[k])

  return merged_list

A = [9,8,4,7,2,3,1,6]
print(merge_sort(A))
