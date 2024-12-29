# Stone Searching

def find_thoul_stone(is_higher_than):
    
    # k를 포함하는 상한값을 찾기 위해 범위를 확장
    low, high = 1, 2
    while is_higher_than(high):  # 상한값을 찾을 때까지 범위를 두 배로 확장
        low = high
        high *= 2

    # 이진 탐색 
    while low < high:
        mid = (low + high) // 2
        if is_higher_than(mid):
            low = mid + 1
        else:
            high = mid

    return low