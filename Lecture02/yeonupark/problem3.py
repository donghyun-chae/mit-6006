# Collage Collating
# -> Doubly Linked List + Sorted Array

class Node:
    def __init__(self, id):
        self.id = id  # 이미지 ID
        self.prev = None  # 이전 노드
        self.next = None  # 다음 노드

class Document:
    def __init__(self):
        self.L = None  # 연결 리스트의 head
        self.tail = None  # 연결 리스트의 tail
        self.S = []  # 정렬된 배열

    # 1. make_document()
    @staticmethod
    def make_document():
        return Document()

    # 2. import_image(x)
    def import_image(self, x):
        # 연결 리스트에 노드를 추가
        new_node = Node(x)
        if self.L is None:  # 연결 리스트가 비어 있으면 초기화
            self.L = new_node
            self.tail = new_node
        else:
            new_node.next = self.L
            self.L.prev = new_node
            self.L = new_node

        # 정렬된 배열에 추가
        # 이진 탐색으로 삽입 위치를 찾음
        index = self.binary_search_insert(x)
        self.S.insert(index, (x, new_node))  # O(n) 삽입

    # 3. display()
    def display(self):
        result = []
        current = self.L
        while current is not None:
            result.append(current.id)
            current = current.next
        return result

    # 4. move_below(x, y)
    def move_below(self, x, y):
        # 배열에서 이진 탐색으로 x와 y를 찾음
        vx = self.binary_search_find(x)
        vy = self.binary_search_find(y)

        if vx is None or vy is None:
            raise ValueError("Invalid image ID")

        # 연결 리스트에서 vx 제거
        if vx.prev:
            vx.prev.next = vx.next
        if vx.next:
            vx.next.prev = vx.prev
        if self.L == vx:
            self.L = vx.next

        # 연결 리스트에서 vy 바로 아래에 vx 삽입
        vx.prev = vy
        vx.next = vy.next
        if vy.next:
            vy.next.prev = vx
        vy.next = vx
        if self.tail == vy:
            self.tail = vx

    # Helper: 이진 탐색으로 삽입 위치 찾기
    def binary_search_insert(self, x):
        low, high = 0, len(self.S)
        while low < high:
            mid = (low + high) // 2
            if self.S[mid][0] < x:
                low = mid + 1
            else:
                high = mid
        return low

    # Helper: 이진 탐색으로 x 찾기
    def binary_search_find(self, x):
        low, high = 0, len(self.S) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.S[mid][0] == x:
                return self.S[mid][1]  # 연결 리스트 노드 반환
            elif self.S[mid][0] < x:
                low = mid + 1
            else:
                high = mid - 1
        return None  # x가 없으면 None 반환
