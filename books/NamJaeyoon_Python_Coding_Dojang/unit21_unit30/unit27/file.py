print('파일 사용하기')
file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()
print(s)
print()

with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

print()

print('multiline write')
with open('hello new.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
print()

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
print('lines write')
with open('line.txt', 'w') as file:
    file.writelines(lines)

print('lines을 리스트로 출력')
with open('line.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print()

print('lines을 한 줄씩 읽기')
with open('line.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

print()

print('for를 이용해서 출력하기')
with open('line.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))


