print('키워드와 딕셔너리')


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


x = {
    'name': '홍길동',
    'age': 30,
    'address': '서울시 용산구 이촌동'
}

# * 를 한번만 넣어주는 경우에는 다른 값이 나온다. 직접 확인해 보자.
personal_info(*x)
personal_info(**x)
print()

print(*x)
# **를 하면 오류가 나오게 된다.
# print(**x)
print()

print('키워드 인수를 사용하는 가변 인수 함수 만들기')


def personal_info_infinity(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ' : ', arg, sep='')


personal_info_infinity(name='길동이')
print()

personal_info_infinity(name='홍길동이', age=30, address='서울시 용산구 이촌동')
print()

personal_info_infinity(**{'name': 'my name is ...'})
print()


def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])


