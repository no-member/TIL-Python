class Person:
    def greeting(self):
        self.hello = '안녕하세요'

maria = Person()
#  maria.hello ## 에러 발생 hello 인스턴스가 아직 생성되지 않았음
maria.greeting()
print(maria.hello)

