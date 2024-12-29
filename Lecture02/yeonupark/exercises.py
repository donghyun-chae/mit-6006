# the number of nodes in cycle

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_cycle_length(head):
    
    # 연결 리스트에서 사이클이 존재할 경우 사이클의 길이를 반환
    # 사이클이 없으면 0을 반환
    
    slow, fast = head, head

    # 1. 사이클 탐지
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # 사이클이 존재하는 경우
            return count_cycle_length(slow)

    return 0  # 사이클이 없는 경우

def count_cycle_length(meeting_point):
    
  # 사이클의 길이를 계산
    current = meeting_point
    cycle_length = 0

    while True:
        current = current.next
        cycle_length += 1
        if current == meeting_point:
            break

    return cycle_length