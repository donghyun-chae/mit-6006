def generate(numRows) :
  answer = [[] for _ in range(numRows)]

  for i in range(numRows):
    if i == 0:
      answer[i] = [1]
    elif i == 1:
      answer[i] = [1,1]
    else :
      for j in range(i):
        if j == 0:
          answer[i].append(1)
        else:
          answer[i].append(answer[i-1][j-1]+answer[i-1][j])
      answer[i].append(1)
  
  return answer

print(generate(5))