print('slice')

a = list(range(0, 100, 10))
print(a)
print(a[0:5])
print(a[0:6:2])
print(a[4:6])
print(a[slice(4, 6)])
print()

print('len을 활용하기')
print(a[:len(a)])
print()

print('슬라이스에 요소 할당하기')
a[4:6] = ['a', 'b', 'c']
print(a)
print('a를 원상태로 되돌림')
a = list(range(0, 100, 10))
print(a)
print('조금만 할당해보기')
a[4:6] = ['a']
print(a)
print('a를 원상태로 되돌림')
a = list(range(0, 100, 10))
print(a)
print('범위보다 더 많이 할당해보기')
a[4:5] = ['a', 'b', 'c', 'd']
print(a)
print()

print('슬라이스와 del')
del a[2:6]
print(a)

