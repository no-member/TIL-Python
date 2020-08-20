print('continue')

for i in range(100):
    if i % 2 == 1:
        continue
    print(i)

print('while with continue')
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
