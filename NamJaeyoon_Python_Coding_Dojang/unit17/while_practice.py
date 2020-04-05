print('while')
i = 0
while i < 100:
    print('Hello world!', i)
    i += 1

print()

i = 100
while i > 0:
    print('Count :', i)
    i -= 1

print()

import random

print('random')
print(random.random())
print(random.random())
print(random.random())
print()

print('randint')
print(random.randint(0, 30))
print(random.randint(0, 30))
print(random.randint(0, 30))
print(random.randint(0, 30))
print()

i = 0
while i != 3:
    i = random.randint(0, 30)
    print(i)
print()

dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
print(random.choice(dice))
print(random.choice(dice))
print(random.choice(dice))
