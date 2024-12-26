class StaticArray:
    def __init__(self, n):
        self.data = [None] * n
    
    def get_at(self, i):
        if not (0 <= i < len(self.data)): raise IndexError
        return self.data[i]
    
    def set_at(self, i, x):
        if not (0 <= i < len(self.data)): raise IndexError
        self.data[i] = x
    
def birthday_match(students):
    n = len(students)
    record = StaticArray(n)
    for k in  range(n):
        (name1, bday1) = students[k]
        for i in range(k):
            (name2, bday2) = record.get_at(i)
            if bday1 == bday2:
                return (name1, name2)
        record.set_at(k, (name1, bday1))
    return None

students = [
    ("윤효전", "01-15"),
    ("채동현", "03-24"),
    ("박연우", "01-15"),
    ("최지인", "07-04"),
    ("김혜다", "07-05")
]

print(birthday_match(students))