a = {1, 2, 3, 4}
b = a
print('a is b')
print(a is b)
print()

b.add(5)
print('a :', a)
print('b :', b)
print()

a = {1, 2, 3, 4}
b = a.copy()
print('a is b')
print(a is b)
print()

b.add(5)
print('a :', a)
print('b :', b)
