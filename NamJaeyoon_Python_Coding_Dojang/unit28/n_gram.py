print('n-gram 만들기')

word = "Hello"
for i in range(len(word) - 1):
    # print(word[i: i+2])
    print(word[i], word[i + 1], sep='')

print()

pharse = "this is python script"
pharse_list = pharse.split()
for i in range(len(pharse_list) - 1):
    print(pharse_list[i], pharse_list[i + 1])

word = "Hello"
two_gram = zip(word, word[1:])
for i in two_gram:
    print(i[0], i[1], sep='')

print()

print(list(zip(word, word[1:])))
print()

print('zip과 리스트 표현식')
word = 'hello'
print([word[i:] for i in range(3)])
range_list = [word[i:] for i in range(3)]
print(list(zip(range_list)))
print(list(zip(*range_list)))

