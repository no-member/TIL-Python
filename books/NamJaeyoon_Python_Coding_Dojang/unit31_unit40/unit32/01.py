def plus_ten(x):
    return x + 10

print(plus_ten(1))
print()

print(lambda x: x + 12)
plus_twelve = lambda x: x + 12
print(plus_twelve(1))
print()

print("람다 표현식 자체를 호출하기")
print((lambda x: x + 10)(1))
print()

print("32.1.2  람다 표현식 안에서는 변수를 만들 수 없다")
# print (lambda x: y = 10; x + y)(1))

y = 13
print((lambda x: x + y)(1))
print()

print("32.1.3  람다 표현식을 인수로 사용하기")
def plus_one(x):
    return x + 1

print(list(map(plus_one, [1, 2, 3])))
print(list(map(lambda x: x + 10, [1, 2, 3])))
print()

print("참고 | 람다 표현식으로 매개변수가 없는 함수 만들기")
print((lambda : 1)())
z = 999
print((lambda : z)())
