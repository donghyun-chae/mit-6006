from linked_list_seq import Linked_List_Seq
from random import randint
from dataclasses import dataclass

Set_from_Seq = lambda x: set(x)

class Hash_Table_Set:
    def __init__(self, r = 200):
        self.chain_set = Set_from_Seq(Linked_List_Seq())
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self): return self.size
    def __iter__(self):
        for X in self.A:
            yield from X
    
    def build(self, X):
        for x in X: self.insert(X)
    
    def _hash(self, k, m):
        return ((self.a * k) % self.p) % m
    
    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100*100 // (self.r*self.r)

    def _resize(self, n):
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100: f += 1
            # f = ceil(r / 100)
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()
    
    def find(self, k):
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)
    
    def insert(self, x):
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added: self.size += 1
        return added
    
    def delete(self, k):
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x
    
    def find_min(self):
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out
    
    def find_next(self, k):
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out
    
    def find_prev(self, k):
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out
    
    def iter_order(self):
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)


@dataclass
class Student:
    def __init__(self, student_id, name):
        self.key = student_id  # Hash_Table_Set이 key 속성을 사용하므로
        self.name = name
    
    def __str__(self):
        return f"Student(ID: {self.key}, Name: {self.name})"

def main():
    # 해시 테이블 생성
    student_db = Hash_Table_Set(r=100)  # r=100으로 설정
    
    # 학생 데이터 삽입
    students = [
        Student(20230001, "Yoon"),
        Student(20230002, "Chae"),
        Student(20230003, "Park"),
        Student(20230004, "Choi"),
        Student(20230005, "Kim")
    ]
    
    # 학생들을 데이터베이스에 추가
    for student in students:
        student_db.insert(student)
        print(f"Inserted: {student}")
    
    print("\nTotal students:", len(student_db))
    
    # 특정 학번으로 학생 찾기
    search_id = 20230003
    found_student = student_db.find(search_id)
    print(f"\nFound student with ID {search_id}:", found_student)
    
    # 정렬된 순서로 모든 학생 출력
    print("\nAll students in order:")
    for student in student_db.iter_order():
        print(student)
    
    # 특정 학번 다음/이전 학생 찾기
    next_student = student_db.find_next(20230002)
    prev_student = student_db.find_prev(20230004)
    print(f"\nNext student after ID 20230002:", next_student)
    print(f"Previous student before ID 20230004:", prev_student)
    
    # 학생 삭제
    deleted_student = student_db.delete(20230001)
    print(f"\nDeleted student:", deleted_student)
    print("Remaining students:", len(student_db))

if __name__ == "__main__":
    main()