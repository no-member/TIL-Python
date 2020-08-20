print('multiple loop')
for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

print()

for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

print()

for i in range(1, 6):
    print('*' * i)
print()

for i in range(5):
    for j in range(5):
        if i == j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()
