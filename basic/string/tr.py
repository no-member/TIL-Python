s = 'abcdeabcde'

print(s.translate(str.maketrans('aeiou', '12345')))
print(s)
