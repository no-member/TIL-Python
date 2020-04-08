print('함수의 호출 과정')


def mul(a, b):
    c = a * b
    return c


def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)


x = 10
y = 20
add(x, y)


def clac(a, b):
    return a + b, a - b, a * b, a / b


print(clac(10, 20))
