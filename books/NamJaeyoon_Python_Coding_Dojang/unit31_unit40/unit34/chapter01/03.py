class Person:
    pass

james = Person()
print(isinstance(james, Person))

def factoral(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1:
        return 1
    return n * factoral(n - 1)

print(factoral(5))
