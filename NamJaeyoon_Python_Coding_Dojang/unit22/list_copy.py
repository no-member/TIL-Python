print('list_copy')
a = [0, 0, 0, 0, 0]
b = a
c = [0, 0, 0, 0, 0]
print('a', a)
print('b', b)
print('c', c)
print()

print('a == b', a == b)
print('a is b', a is b)
print()

print('a == c', a == c)
print('a is c', a is c)
print()

print('b[2] = 99')
b[2] = 99
print('a', a)
print('b', b)
print()

print('b = a.copy()')
a = [0, 0, 0, 0, 0]
b = a.copy()
print('a == b', a == b)
print('a is b', a is b)
print()

print('a', a)
print('b', b)
print()

b[2] = 99
print('a', a)
print('b', b)
print()
