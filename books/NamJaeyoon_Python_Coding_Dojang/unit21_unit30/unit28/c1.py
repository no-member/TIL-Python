palindrome = 'hohoh'
no_palindrome = 'sh'

# # for문을 이용한 회문 판독
# is_palindrome = True
# for i in range(len(palindrome) // 2):
#     if palindrome[i] != palindrome[-1 - i]:
#         is_palindrome = False
#         break
#
# print(is_palindrome)


# # 시퀀스 뒤집그를 이용한 검사방법
# print(palindrome == palindrome[::-1])
# print(no_palindrome == no_palindrome[::-1])

# # list 와 reversed 이용하기
# print(list(palindrome) == list(reversed(palindrome)))
# print(list(no_palindrome) == list(reversed(no_palindrome)))

# reversed와 join 활용하기
print(palindrome == ''.join(reversed(palindrome)))
print(no_palindrome == ''.join(reversed(no_palindrome)))
