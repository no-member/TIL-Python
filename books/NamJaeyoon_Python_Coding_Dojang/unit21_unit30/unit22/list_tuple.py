print('튜플 응용하기')
a = (38, 21, 53, 62, 19, 53)
print('튜플안의 요소 인덱스 구하기')
print('a.index(53)', a.index(53))
print()

print('튜플안의 요소 개수 구하기')
print('a.count(20)', a.count(20))
print()

print('튜플 출력하기')
for i in a:
    print(i, end=' ')

print()
print()

print('튜플 표현식 사용하기')
b = tuple(i for i in range(10) if i % 2 == 0)
print(b)
print()

c = (i for i in range(10) if i % 2 == 1)
print(c)
print()

d = (1.2, 2.5, 3.7, 4.6)
d = map(int, d)
print('d :', d)
print('tuple(d) :', tuple(d))
print()

f = (38, 21, 53, 62, 19)
print('f :', f)
print('min(f) :', min(f))
print('max(f) :', max(f))
print('sum(f) :', sum(f))
print()


