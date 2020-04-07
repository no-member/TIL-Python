print('딕셔너리 표현식')

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print('x :', x)
print()

y = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
print('y :', y)
print()

z = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()}
print('z :', z)
print()

a = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(a)

# for key, value in a.items():
#     if value == 20:
#         del a[key]
#
# print('a', a)

a = {key: value for key, value in a.items() if value != 20}
print(a)
