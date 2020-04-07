print('딕셔너리 복사하기')

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x

print(x is y)
print()

y['a'] = 99
print('y :', y)
print('x :', x)

a = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
b = a.copy()

print('a is b :', a is b)
print('a == b :', a == b)
print()

b['a'] = 99
print('a :', a)
print('b :', b)
print()

c = {
    'a': {
        'python': '2.7'
    },
    'b': {
        'python': '3.6'
    }
}

d = c.copy()

print('c is d : ', c is d)
print('c == d :', c == d)
print()

c['a']['python'] = '2.1.3'
print('c :', c)
print('d :', d)
print()

e = {
    'a': {
        'python': '2.7'
    },
    'b': {
        'python': '3.6'
    }
}

import copy

f = copy.deepcopy(e)
f['a']['python'] = '2.7.5'
print('e :', e)
print('f :', f)
print()
