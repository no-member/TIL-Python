print('diction')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print('x :', x)
print()

x.setdefault('e')
print('setdefault x :', x)
print()

x.setdefault('f', 100)
print('setdefault x :', x)
print()

x.update(a=100)
print('after update x :', x)
print()

y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print('y :', y)
print()

y.update(a=100)
print('y :', y)
print()

y.update(e=50)
print('y :', y)
print()

y.update(a=900, f=60)
print('y :', y)
print()

z = {1: 'one', 2: 'two'}
print('z :', z)
print()

z.update({1: 'ONE', 3: 'THREE'})
print(z)
print()

z.update([[2, 'TWO'], [4, 'FOUR']])
print(z)
print()

z.update(zip([1, 2], ['one', 'two']))
print(z)
print()

print('값 삭제하기')
a = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(a.pop('a'))
print(a)
print()

print(a.pop('z', 0))
print(a)
print()

del a['b']
print(a)
print()

print('랜덤 혹은 마지막 값 삭제하기')
b = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(b.popitem())
print(b)
print()

print(b)
print()

c = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(c.get('c'))
print()

print(c.get('z'))
print(c.get('z', 0))
print()

print(c.items())
print(c.keys())
print(c.values())
print()

print('list와 tuple로 dictionary 만들기')
keys = ['a', 'b', 'c', 'd']
d = dict.fromkeys(keys)
print(d)

e = dict.fromkeys(keys, 100)
print(e)

print(e['a'])
print()

print('defualtdict 사용하기')
from _collections import defaultdict

f = defaultdict(int)
print(f['z'])
