class Student:  # outer class

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # inner class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self): print(self.brand, self.cpu, self.ram)


s1 = Student('Ahroo', '25186')
s2 = Student('barbossa', '170020C')

lap1 = s1.lap
lap2 = s2.lap

s1.show()
