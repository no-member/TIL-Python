print('for과 dictionary')
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for i in x:
    print(i, end='')
print()

for key, value in x.items():
    print(key, value)
print()

for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)
print()

print('key만 출력하기')

for key in x.keys():
    print(key, end=' ')
print()

print('value만 출력하기')

for value in x.values():
    print(value, end=' ')
print()
