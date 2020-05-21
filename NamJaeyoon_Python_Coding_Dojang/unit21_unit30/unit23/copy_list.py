a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)
print()

c = [[10, 20], [30, 40]]
d = c.copy()
c[0][0] = 400
print(c)
print(d)
print()

f = [[10, 20], [30, 40]]
import copy

g = copy.deepcopy(f)
f[0][0] = 600
print(f)
print(g)
print()
