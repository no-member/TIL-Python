print('for과 list')

print(1)
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y)

print()

print(2)
for i in a:
    for j in i:
        print(j, end=' ')
    print()

print()

print(3)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

print()

print(4)
i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1

print()

print(5)
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

print()
