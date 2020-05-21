print('이차원 리스트')
a = [
    [10, 20]
    , [30, 40]
    , [50, 60]
]
print(a)
print()

print('a[0][0] :', a[0][0])
print('a[0] :', a[0])
print()

print('톱니형 리스트')
b = [
    [10, 20]
    , [500, 800, 200]
    , [9]
    , [30, 20]
    , [200, 444, 1111, 2232]
]

print(b)
print()

print('pprint')
from pprint import pprint
pprint(a, indent=4, width=20)
print()
pprint(b, indent=0, width=40)


