def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
print()

personal_info(*x)
print()


def personal_info2(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')


personal_info2(name='홍길동2')
print()
personal_info2(name='홍길돌3', age=40, address='서울시 용산구 어딘가2')
print()
personal_info2(**x)


def personal_info3(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])
