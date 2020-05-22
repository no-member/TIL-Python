print('unpacking 연습')

print(10, 20, 30)


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


x = [10, 20, 30]
print_numbers(*x)
print()

print('가변 인수 함수')


def print_nubmers2(*args):
    for arg in args:
        print(arg)


print_nubmers2(10)
print()

print_nubmers2(10, 20, 30, 40)
print()

x = [10]
print_nubmers2('x', *x)
print()

y = [10, 20, 30, 40]
print_nubmers2('y', *y)
print()




