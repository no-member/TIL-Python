print('map 사용하기')

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)
print()

b = [1.2, 2.5, 3.7, 4.6]
b = list(map(int, b))
print(b)
print()

c = list(map(str, range(10)))
print(c)
print()

d = input('두개의 문자를 입력해 주세요.').split()
print(d)
print()

f = map(int, input('두개의 숫자를 입력해 주세요.').split())
print('f :', f)
print('list(f) :', list(f))
print()

