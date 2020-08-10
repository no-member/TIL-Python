def greeting():
    print('Outside Hello')

class Person:
    def greeting(self):
        print('Inside_Hello')

    def inside_hello(self):
        self.greeting()

    def outside_hello(self):
        greeting()


james = Person()

print("outside_hello")
james.outside_hello()
print()

print("inside_hello")
james.inside_hello()
