n = int(input())
nums = list(map(int, input().split()))
nums.sort()
good = 0  # 좋은 수의 개수를 세는 변수

# 각 숫자에 대해 검사
for i in range(n):  # i는 현재 검사하는 '타겟' 숫자의 인덱스
    left = 0  # 왼쪽 포인터
    right = n-1  # 오른쪽 포인터
    
    while left < right:
        # 현재 검사하는 숫자(i번째 수)는 제외
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
            
        current_sum = nums[left] + nums[right]
        if current_sum == nums[i]:  # 두 수의 합이 타겟 숫자와 같다면
            good += 1  # 좋은 수 카운트 증가
            break  # 하나만 찾으면 되므로 break
        elif current_sum < nums[i]:  # 합이 작으면 왼쪽 포인터를 증가
            left += 1
        else:  # 합이 크면 오른쪽 포인터를 감소
            right -= 1

print(good)