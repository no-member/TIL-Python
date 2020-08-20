class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print(f'이제 {self.__wallet}원 남아있습니다.')

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
