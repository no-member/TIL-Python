class Person():
    def __init__(self):
        print('Person')

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()
        self.school = '파이썬 코딩 도장'


