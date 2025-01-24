class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update() AVL트리에서 다룰 예정
    
def subtree_iter(A):    # O(n) 트리 순회
    if A.left: yield from A.left.subtree_iter()
    yield A
    if A.right: yield from A.right.subtree_iter()

def subtree_first(A):    # O(h) 첫번째 노드 찾기
    if A.left: return A.left.subtree_first()
    else: return A

def subtree_last(A):    # O(h) 마지막 노드 찾기
    if A.right: return A.right.subtree_last()
    else: return A

def successor(A):    # O(h) 중위 순회 순서상 다음 순서 노드 찾기
    if A.right: return A.right.subtree_first()
    while A.parent and (A is A.parent.right):
        A = A.parent
    return A.parent

def predecessor(A):    # O(h) 중위 순회 순서상 이전 순서 노드 찾기
    if A.left: return A.left.subtree_last()
    while A.parent and (A is A.parent.left):
        A = A.parent
    return A.parent

def subtree_insert_before(A, B): # O(h) A 이전 순서에 B 삽입
    if A.left:
        A = A.left.subtree_last()
        A.right, B.parent = B, A
    else:
        A.left, B.parent = B, A
    # A.maintain() AVL트리에서 다룰 예정

def subtree_insert_after(A, B): # O(h) A 이후 순서에 B 삽입
    if A.right:
        A = A.right.subtree_first()
        A.left, B.parent = B, A
    else:
        A.right, B.parent = B, A

def subtree_delete(A):    # O(h) 삭제
    if A.left or A.right:    # A가 리프가 아닌 경우
        if A.left: B = A.predecessor()
        else: B = A.successor()
        A.item, B.item = B.item, A.item
        return B.subtree_delete()
    
    if A.parent:    # A가 리프인 경우
        if A.parent.left is A: A.parent.left = None
        else: A.parent.right = None
        # A.parent.maintain() AVL트리에서 다룰 예정
    return A