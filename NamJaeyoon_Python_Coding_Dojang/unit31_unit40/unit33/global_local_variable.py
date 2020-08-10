print("# 33.1.1  함수 안에서 전역 변수 변경하기")

x = 10
def foo():
    x = 20
    print(x)

foo()
print(x)
