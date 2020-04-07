print('리스트 응용')
a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

a.append(40)
print('a :', a)
print('len(a) :', len(a))
print()

print('빈 리스트')
a = []
print('a :', a)
print('len(a) :', len(a))
print()

a.append(10)
print('a :', a)
print('len(a) :', len(a))
print()

print('리스트 안에 리트트 넣기')
a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

a.append([500, 600])
print('a :', a)
print('len(a) :', len(a))
print()

print('extend')
a = [10, 20, 30]
a.extend([500, 600])
print('a :', a)
print('len(a) :', len(a))
print()

print('insert')
a = [10, 20, 30]
a.insert(1, 100)
print('a :', a)
print('len(a) :', len(a))
print()

print('리스트 가장 앞에 요소를 추가하는 방법')
a.insert(0, 0)
print('a :', a)
print('len(a) :', len(a))
print()

print('리스트 마지막에 insert를 통해서 넣는 방법')
a.insert(len(a), 999)
print('a :', a)
print('len(a) :', len(a))
print()

print('리스트 중간에 여러 요소를 넣는 방법')
a[1:1] = [200, 300, 400]
print('a :', a)
print('len(a) :', len(a))
print()

a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

print('pop 사용하기')
a.pop()
print('a :', a)
print('len(a) :', len(a))
print()

a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

print('pop에 인덱스로 삭제하기')
a.pop(1)
print('a :', a)
print('len(a) :', len(a))
print()

a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

print('del을 이용해서 삭제하기')
del a[1]
print('a :', a)
print('len(a) :', len(a))
print()

a = [10, 20, 30]
print('a :', a)
print('len(a) :', len(a))
print()

print('remove를 사용해서 리스트의 특정 값을 삭제하기')
a.remove(30)
print('a :', a)
print('len(a) :', len(a))
print()

a = [10, 20, 30, 20]
print('a :', a)
print('len(a) :', len(a))
print()

print('중복시 remove를 사용한 경우')
a.remove(20)
print('a :', a)
print('len(a) :', len(a))
print()

print('index 값 구하기')
print(a)
print('a.index(30) :', a.index(30))
print()

print('중복시 index 값을 사용한 경우')
a = [10, 20, 30, 20]
print(a)
print('a.index(20) :', a.index(20))
print()

print('count')
print(a)
print('a.count(20) :', a.count(20))
print()

print('리스트 순서 뒤집기')
a.reverse()
print('a :', a)
print()

print('리스트를 정렬하기 sort')
a.sort()
print('a :', a)
print()

print('sorted(b)')
b = [10, 30, 15, 77, 40]
print('b :', b)
print('sorted(b) :', sorted(b))
print('b :', b)

print('clear')
print('a :', a)
a.clear()
print('a :', a)
print()

print('빈 객체를 확인하는 방법')
if a:
    print('비어 있지 않습니다.')
else:
    print('비어 있습니다.')

