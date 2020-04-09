print('keyword')


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


print('출력 1')
personal_info('홍길동', 30, '서울시 용산구 이촌동')
print()

print('출력 2')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
print()

print('출력 3')
personal_info(age=30, name='홍길동', address='서울시 용산구 이촌동')
print()


