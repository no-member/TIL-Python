class Person:
    pass

james = Person()
print(isinstance(james, Person))
print()

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)
