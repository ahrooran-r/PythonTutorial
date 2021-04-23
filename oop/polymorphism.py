class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return [m1, m2]


s1 = Student(56, 73)
s2 = Student(66, 68)

print(s1 + s2)  # -> Student.__add__(s1, s2)
