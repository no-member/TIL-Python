print('회문 구하기')

print('for을 사용한 회문 찾기')
word = input('단어를 입력하세요: ')

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_palindrome = False
        break
print(is_palindrome)

print('reversed 함수와 join을 이용한 회문 찾기')
word = input('다른 단어를 입력해주세요: ')
is_palindrome = True
if word != ''.join(reversed(word)):
    is_palindrome = False
print(is_palindrome)


print('시퀀스 뒤집기를 사용한 방법')
word = input('또 다른 단어를 입력해 주세요. :')
is_palindrome = True
if word != word[::-1]:
    is_palindrome = False
print(is_palindrome)
print()


print('reversed 함수를 이용한 회문 찾기')
word = input('다시 단어를 입력해 주세요 :')
is_palindrome = True
if list(word) != list(reversed(word)):
    is_palindromes = False
print(is_palindrome)
