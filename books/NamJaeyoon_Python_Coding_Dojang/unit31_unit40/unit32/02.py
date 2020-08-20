print("32.2.1  람다 표현식에 조건부 표현식 사용하기")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))
print()

# list(map(lambda x: str(x) if x % 3 == 0, a))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x == 1 else float(2) if x == 2 else x + 10, a)))
print()

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(f, a)))
print()

print("32.2.2  map에 객체를 여러 개 넣기")
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)))
print()

print("32.2.3  filter 사용하기")

def test_filter(x):
    return 5 < x and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(test_filter, a)))
print()

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: 5 < x and x < 10, a)))
print()

print("reduce")
def reduce_test(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(reduce_test, a))
print()

a = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, a))
print()

print("참고 | map, filter, reduce와 리스트 표현식")
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print([i for i in a if 5 < i and i < 10])
print()

a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) - 1):
    x = x + a[i + 1]

print(x)
