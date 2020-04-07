print('리스트 표현식')
a = [i for i in range(10)]
print(a)
print()

b = list(i for i in range(10))
print(b)
print()

c = [i + 5 for i in range(10)]
print(c)
print()

d = [i * 2 for i in range(10)]
print(d)
print()

print('리스트 표현식에서 if 사용하기')
A = [i for i in range(10) if i % 2 == 0]
print(A)
print()

B = [i + 5 for i in range(10) if i % 2 == 1]
print(B)
print()


