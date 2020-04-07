print('String의 메서드')

print('문자열을 다른 문자열로 바꾸기')
print('Hello, world!'.replace('world', 'Python'))
print()

s = 'Hello, world'
s = s.replace('world', 'Python')
print(s)
print()

print('문자를 특정 문자로 바꾸기')
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
print()

print('문자열을 리스트로')
fruit = 'apple pear grape pineapple orange'.split()
print(fruit)
print()

fruit2 = 'apple, pear, grape, pineapple, orange'.split(', ')
print(fruit2)
print()

print('리스트의 요소를 문자열로')
fruit3 = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(fruit3)
print()

fruit4 = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(fruit4)
print()

print('대문자, 소문자 바꾸기')
print('python'.upper())
print()

print('PYTHON'.lower())
print()

print('문자열 공백 없애기')
print('  Python  '.lstrip())
print()

print('  Python  '.rstrip())
print()

print('  Python  '.strip())
print()

print(',  python. '.lstrip(',.'))
print()

print(',  python.'.rstrip(',.'))
print()

import string
print(', python.'.strip(string.punctuation))
print(string.punctuation)
print()

print(', python. '.strip(string.punctuation + ' '))
print()

print('문자열 정렬하기')
print('python'.ljust(10))
print()

print('python'.rjust(10))
print()

print('python'.center(10))
print()

print('python'.center(11))
print()

print('메서드 체이닝')
print('python'.rjust(10).upper())
print()

print('공백에 0을 채우기')
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))
print()

print('index 찾기')
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))
print()

print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))
print()

print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))
print('apple pineapple'.count('pl'))
print()


