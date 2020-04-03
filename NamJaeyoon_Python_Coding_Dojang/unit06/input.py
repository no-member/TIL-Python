print('input 함수')
print(input())

x = input('x에 넣을 값을 입력해 주세요')
print("x의 값은", x)

a = int(input('첫 번째 값을 입력해주세요.'))
b = int(input('두 번째 값을 입력해주세요.'))
print('두 값의 핪은 : ', a + b)

print('두개의 문자열을 입력 받기')
a, b = input('문자열 두개를 입력해 주세요').split()
print('첫번째 문자는 ', a)
print('두번째 문자는 ', b)
print('첫번째 문자와 두번쨰 문자의 합은 ', a + b)

print('map을 이용해서 여러개 입력 받은 값을 정수로 변화시키기')
x, y = map(int, input('숫자 x와 y 값을 입력해 주세요').split())
print('x + y는 ', x + y)
