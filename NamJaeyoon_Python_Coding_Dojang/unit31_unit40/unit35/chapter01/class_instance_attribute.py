class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)

