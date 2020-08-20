print(10, 20, 30)
print()


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


print_numbers(10, 20, 30)
print()

x = [10, 20, 30]
print_numbers(*x)
print()


def print_numbers2(*args):
    for arg in args:
        print(arg)


print_numbers2(10)
print()
print_numbers2(10, 20, 30, 40)
print()

x = [10]
print_numbers2(*x)
print()

y = [10, 20, 30, 40, 50]
print_numbers2(*y)


def print_numbers3(a, *args):
    print(a)
    print(args)


print_numbers3(1)
print_numbers3(1, 10, 20)
print_numbers3(*[10, 20, 30])
