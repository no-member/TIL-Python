class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

    def greeting(self):
        print(f'my name is {self.name}, {self.age} years old')


maria = Person('마리아', 26, '서울시 서초구 반포동')
maria.greeting()

kim = Person(*['킴', 99, '목성'])
kim.greeting()

# shin = Person()
# shin.greeting()
