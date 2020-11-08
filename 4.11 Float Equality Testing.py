from math import isclose

x = 0.1 + 0.1 + 0.1
a = 0.3
print(x == a)
print(format(x, '.25f'))
print(format(a, '.25f'))
print(round(x) == round(a))

y = 0.125 + 0.125 + 0.125
z = 0.375
print(y == z)

x = 10000.01
y = 10000.02

delta = 0.1

a = 0.01
b = 0.01
delta2 = 0.1
print(round(a) == round(b))


x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))

x = 123456.1
y = 123456.2
print(isclose(x, y, rel_tol=0.01))

x = 0.1
y = 0.2
print(isclose(x, y, rel_tol=0.01))

x = 0.000001
y = 0.000002
print(isclose(x, y, rel_tol=0.01))
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))

