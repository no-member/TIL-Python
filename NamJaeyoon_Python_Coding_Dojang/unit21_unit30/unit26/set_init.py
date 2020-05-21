print('set 만들기')

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

print('중복된 set')
fruits = {'orange', 'strawberry', 'orange'}
print(fruits)

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

print('in')
print('orange' in fruits)
print('peach' in fruits)
print()

print('not in')
print('orange' not in fruits)
print('peach' not in fruits)
print()

print('set을 이용해서 세트 만들기')
a = set('apple')
print('a :', a)
print()

b = set(range(5))
print('b :', b)
print()

c = set()
print('c :', c)
print()

d = {}
print('d :', d)
print()

print('set()과 {}로 만들어진 것의 타입 비교')
print('type(set()) :', type(c))
print('type({}) :', type(d))
print()

print('프로즌 세트')
e = frozenset(range(10))
print(e)
