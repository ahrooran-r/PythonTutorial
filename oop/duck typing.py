class Laptop:
    def code(self, ide):
        ide.execute()


class PyCharm:
    def execute(self):
        print('compiling')
        print('running')


class MyEditor:
    def execute(self):
        print('spell check')
        print('convention check')
        print('compiling')
        print('running')


ide = PyCharm()
ide = MyEditor()  # we can change ide as long as it provides the same execute method

lap1 = Laptop()
lap1.code(ide)
