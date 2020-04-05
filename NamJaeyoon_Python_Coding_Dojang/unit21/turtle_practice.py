import turtle as t

t.shape('turtle')

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

for i in range(4):
    t.fd(100)
    t.rt(90)

n = int(input('몇 각형을 그리겠습니까?'))

for i in range(n):
    t.fd(100)
    t.rt(360 / n)


