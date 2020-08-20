a = [38, 21, 53, 62, 19]

print('list와 for')
for i in a:
    print(i)

print()

print('인데스와 요소를 함께 출력하기')
for index, value in enumerate(a):
    print(index, value)

print()

print('인덱스를 1부터 시작하고 싶은 경우')
for index, value in enumerate(a):
    print(index + 1, value)

print()

for index, value in enumerate(a, start=1):
    print(index, value)

print()

print('while')
a = [20, 51, 22, 60, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1


