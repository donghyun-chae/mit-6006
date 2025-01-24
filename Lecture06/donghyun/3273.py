n = int(input())
nums = list(map(int, input().split()))
x = int(input())

cnt = 0
nums.sort()

i = 0
j = len(nums) - 1
while i < j:
    if nums[i] + nums[j] > x:
        j -= 1
    elif nums[i] + nums[j] < x:
        i += 1
    else: 
        cnt += 1
        i += 1 
        j -= 1

print(cnt)