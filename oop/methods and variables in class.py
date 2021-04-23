class School:
    name = 'JHC'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): return (self.m1 + self.m2 + self.m3) // 3

    @classmethod
    def school_name(cls): return cls.name

    @staticmethod
    def info(): return 'This is School class in xxx module'


s1 = School(41, 83, 45)
s2 = School(66, 73, 93)

print(School.info())
print(s2.avg())
