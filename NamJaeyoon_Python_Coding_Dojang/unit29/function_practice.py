print('함수')


def hello():
    print('Hello, world!')


hello()
print()


def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    print(a + b)


add(1, 3)
print(add.__doc__)
print()


def add(a, b):
    return a + b


x = add(1, 2)
print(x)


def one():
    return 1


print(one())


def add_sub(a, b):
    return a + b, a - b


x, y = add_sub(10, 30)
print(x, y)

x = add_sub(10, 30)
print(x)
print()


def one_two():
    """1, 2 와 (1, 2) 어느 쪽이든 상관이 없다."""
    return 1, 2


print(one_two())

