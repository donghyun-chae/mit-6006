'''
Exercise: Given an array of items A = (a0, . . . , an−1), describe a O(n)-time algorithm to construct a binary tree T containing the items in A such that (1) the item stored in the i
th node of T’s
traversal order is item ai, and (2) T has height O(log n). 

연습문제:
주어진 배열 A = (a0, ..., an-1)에 대해, 다음 조건을 만족하는 이진 트리 T를 O(n) 시간에 구성하는 알고리즘을 설명하시오:

T의 순회 순서에서 i번째 노드에 저장된 항목이 ai임
T의 높이가 O(log n)임
'''

def build_balanced_tree(A):
    def build_recursive(start, end):
        if start >= end:
            return None
        
        mid = (start + end) // 2
        node = Binary_Node(A[mid])
        
        # 왼쪽 서브트리 생성
        node.left = build_recursive(start, mid)
        if node.left:
            node.left.parent = node
            
        # 오른쪽 서브트리 생성
        node.right = build_recursive(mid + 1, end)
        if node.right:
            node.right.parent = node
            
        return node
    
    tree = Binary_Tree()
    tree.root = build_recursive(0, len(A))
    tree.size = len(A)
    return tree