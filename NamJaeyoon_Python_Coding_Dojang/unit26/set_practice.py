print('세트 조작하기')
a = {1, 2, 3, 4}
print('a', a)
print('a.add(5) :', a.add(5))
print('a', a)
print()

print('a.remove(3)', a.remove(3))
print('a', a)
# print('a.remove(3)', a.remove(3))
# 에러 발생
# print('a', a)

print('a.discard(2) :', a.discard(2))
print(a)
print('a.discard(3) :', a.discard(3))
print(a)
print()

a = {1, 2, 3, 4}
print('a', a)
print(a.pop())
print('a', a)
print(a.pop())
print('a', a)
print()

a = {1, 2, 3, 4}
print('a', a)
print('a.clear() :', a.clear())
print(a)
print()

a = {1, 2, 3, 4}
print('a', a)
print(len(a))
print()

