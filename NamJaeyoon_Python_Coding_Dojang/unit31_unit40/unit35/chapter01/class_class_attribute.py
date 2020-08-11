class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('Book')

maria = Person()
maria.put_bag('Key')

print(james.bag)
print(maria.bag)
print()

print(james.__dict__)
print(Person.__dict__)
print()
