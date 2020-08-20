def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('홍길동', 30, '서울시 용산구 어딘가1')
print()

personal_info(name='홍길동2', age=40, address='서울시 용산구 어딘가2')
print()


personal_info(age=50, name='홍길동3', address='서울시 용산구 어딘가3')
print()

print(10, 20, 30, sep=':', end='')

