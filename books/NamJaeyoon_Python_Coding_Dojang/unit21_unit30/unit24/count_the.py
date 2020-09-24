count_the = input().split(' ')
only_word_list = []

import string

for input_to in count_the:
    only_word_list.append(input_to.strip(string.punctuation))

print(only_word_list.count('the'))

