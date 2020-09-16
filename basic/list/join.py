li = [1, 2, 'hi'] 
print(li)
# print('-'.join(li)) 파이썬은 문자와 숫자를 join으로 직접 연결 할 수 없다.
print('-'.join(list(map(str, li))))
print(li)

