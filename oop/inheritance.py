class A:

    def __init__(self):
        print('init A')

    def feature1(self): print('feature 1-A')

    def feature2(self): print('feature 2')


class B:

    def __init__(self):
        print('init B')

    def feature1(self): print('feature 1-B')

    def feature4(self): print('feature 4')


class C(A, B):

    def __init__(self):
        super().__init__()
        print('init C')

    def feature5(self): print('feature 5')


# a1 = A()
c1 = C()
c1.feature1()
