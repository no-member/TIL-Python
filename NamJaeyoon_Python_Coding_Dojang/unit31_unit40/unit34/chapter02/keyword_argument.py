class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

    def greeting(self):
        print(f'My name is {self.name}, {self.age} years old')

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria1.greeting()
print()

maria2 = Person(**{'name': '마리아2', 'age': 20, 'address': '서울시 서초구 반포동'})
maria2.greeting()
print()
