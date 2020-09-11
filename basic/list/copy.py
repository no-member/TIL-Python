a = [10, 20, 30, 40]

print('얕은 복사')
b = a
print(b)
print(a == b)
print(a is b)
print()

a.append(50)
print(a)
print(b)
print()

c = [10, 20]
print('깊은 복사')
d = c.copy()
print(d)
print(c == d)
print(c is d)
print()

c.append(30)
print(c)
print(d)
print()
