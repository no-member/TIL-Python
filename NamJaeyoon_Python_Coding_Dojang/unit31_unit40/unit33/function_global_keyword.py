print("33.1.1  함수 안에서 전역 변수 변경하기")
print()

x = 10
def foo():
    global x
    x = 20
    print("inside function")
    print(x)

foo()
print("outside function")
print(x)
