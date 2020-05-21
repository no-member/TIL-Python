print('format')
print('I an %s.' % 'james')
print()

name = 'maria'
print('I am %s' % name)
print()

print('%f' % 2.3)
print()

print('%.2f' % 2.3)
print()

print('%.3f' % 2.3)
print()

print('%10s' % 'python')
print()

print('%10d' % 15)
print()

print('%10d' % 1000)
print()

print('%2.3f' % 2.3)
print('%10.2f' % 2000.3)
print()

print('%-10s' % 'python')
print()

print('서식 지정자로 문자열 안에 값 여러 개 넣기')
print('Today is %d %s.' % (3, 'April'))
print()

print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))
print()

print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
print()

print('{0} {0} {1} {1}'.format('Python', 'Script'))
print()

print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
print()

print('Hello, {language} {version}'.format(language='Python', version=3.6))
print()

print('{{ {0} }}'.format('Python'))
print()

print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))
print()

print('%03d' % 1)
print('{0:03d}'.format(35))
print()

print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))
print()

print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))
print()

print(format(148930293450, ','))
print('%20s' % format(147892179, ','))
print()
