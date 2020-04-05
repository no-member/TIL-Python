print('FizzBuzz')
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    if i % 3 == 0:
        print('Fizz')
        continue
    if i % 5 == 0:
        print('Buzz')
        continue
    print(i)

print('골프 방식')
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

