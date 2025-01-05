"""
Problem 1-4. Jen & Berry’s
Jen drives her ice cream truck to her local elementary school at recess. All the kids rush to line up
in front of her truck. Jen is overwhelmed with the number of students (there are 2n of them), so
she calls up her associate, Berry, to bring his ice cream truck to help her out. Berry soon arrives
and parks at the other end of the line of students. He offers to sell to the last student in line, but the
other students revolt in protest: “The last student was last! This is unfair!”
The students decide that the fairest way to remedy the situation would be to have the back half of
the line (the n kids furthest from Jen) reverse their order and queue up at Berry’s truck, so that the
last kid in the original line becomes the last kid in Berry’s line, with the (n+1)st kid in the original
line becoming Berry’s first customer.
    (a) Given a linked list containing the names of the 2n kids, in order of the original line
formed in front of Jen’s truck (where the first node contains the name of the first kid in
line), describe an O(n)-time algorithm to modify the linked list to reverse the order of
the last half of the list. Your algorithm should not make any new linked list nodes or
instantiate any new non-constant-sized data structures during its operation.

    (b) Write a Python function reorder students(L) that implements your algorithm. 
"""

# (a)
# 1. 더블 링크드 리스트로 해결 (X)
# --> instantiate any new non-constant-sized data structures during its operation. 이 규칙에 위배됨
# 2. fast/slow 활용 (O)
# --> 앞선 문제에서 언급된 fast/slow 알고리즘을 활용하여 하나의 포인터는 2번씩 next node 로 이동하고 하나의 포인터는 1번씩 이동하여
# 먼저 가는 노드가 끝에 도달하면 중간지점을 얻을 수 있고 그 중간 지점부터 하나씩 포인터 수정

def reorder_students(L):
    '''
    Input: L | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
    - any additional linked list nodes
    - any other non-constant-sized data structures
    '''
    if not L.head or not L.head.next:
        return
    
    slow = fast = L.head
    mid = None 

    while fast and fast.next:
        fast = fast.next.next
        mid = slow
        slow = slow.next
    
    current = slow
    prev_node = None
    
    while current:
        next_temp = current.next
        current.next = prev_node
        prev_node = current
        current = next_temp

    if mid:
        mid.next = prev_node
