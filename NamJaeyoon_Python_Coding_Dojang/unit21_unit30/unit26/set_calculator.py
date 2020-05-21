print('set calculator')

print('합집합 | , set.union')
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print('a :', a)
print('b :', b)
print('a | b :', a | b)
print('set.union(a, b) :', set.union(a, b))
print()

print('교집합  &, set.intersection(a, b)')
print('a :', a)
print('b :', b)
print('a & b :', a & b)
print('set.intersection(a, b) :', set.intersection(a, b))
print()

print('차집합 -, set.difference(a, b)')
print('a :', a)
print('b :', b)
print('a - b :', a - b)
print('set.difference(a, b) :', set.difference(a, b))
print()

print('대칭차집합 a ^ b, set.symmetric_difference(a, b)')
print('a :', a)
print('b :', b)
print('a ^ b :', a ^ b)
print('set.symmetric_difference(a, b) :', set.symmetric_difference(a, b))
print()

print('집합 연산 후 할당 연산자 사용하기')
a = {1, 2, 3, 4}
print('a :', a)
print('a |= {5} :')
a |= {5}
print(a)
print()

a = {1, 2, 3, 4}
print(a)
print('a.update({5}) :', a.update({5}))
print(a)
print()

a = {1, 2, 3, 4}
print(a)
print('a &= {0, 1, 2, 3} :')
a &= {0, 1, 2, 3}
print(a)
print()

a = {1, 2, 3, 4}
print(a)
print('a.intersection_update({0, 1, 2, 3}')
print(a.intersection_update({0, 1, 2, 3}))
print(a)
print()

a = {1, 2, 3, 4}
print(a)
print('a -= {3}')
a -= {3}
print(a)
print()

a = {1, 2, 3, 4}
print(a)
print('a.difference_update({3}) :', a.difference_update({3}))
print(a)
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a ^= {3, 4, 5, 6}')
a ^= {3, 4, 5, 6}
print('a :', a)
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a.symmetric_difference_update({3, 4, 5, 6})', a.symmetric_difference_update({3, 4, 5, 6}))
print(a)
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a <= {1, 2, 3, 4} :', a <= {1, 2, 3, 4})
print('a <= {1, 2, 3, 4, 5} :', a <= {1, 2, 3, 4, 5})
print('a.issubset({1, 2, 3, 4, 5}) :', a.issubset({1, 2, 3, 4, 5}))
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a < {1, 2, 3, 4} :', a < {1, 2, 3, 4})
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a >= {1,2,3,4} :', a >= {1, 2, 3, 4})
print('a.issuperset({1,2,3,4}) :', a.issubset({1, 2, 3, 4}))
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a == {1, 2, 3, 4} :', a == {1, 2, 3, 4})
print('a != {1, 2, 3, 4} :', a != {1, 2, 3, 4})
print('a == {1, 2, 3} :', a == {1, 2, 3})
print('a != {1, 2, 3} :', a != {1, 2, 3})
print()

a = {1, 2, 3, 4}
print('a :', a)
print('a.isdisjoint({5, 6, 7, 8}) :', a.isdisjoint({5, 6, 7, 8}))
print('a.isdisjoint({3, 4, 5, 6}) :', a.isdisjoint({3, 4, 5, 6}))
print()

