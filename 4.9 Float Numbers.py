from fractions import Fraction

# x = float('22/7')
# print(x)

y = float(Fraction('22/7'))
print(y)

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
print(format(a, '.25f'))
print(format(b, '.25f'))
# this is because 0.3 has not exact representation  in binary 2

