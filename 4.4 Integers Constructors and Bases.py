from decimal import Decimal

a = int(10.9)
print(a)
b = int(-10.9)
print(b)
# truncation
c = int(True)
print(c)
d = int(Decimal("10.9"))
print(d)
e = int('10')
print(e)
f = int('1010', base=2)
print(f)
g = int('AF21', base=16)
print(g)
# max base is 36 0 to z
print(bin(10))
print(oct(10))
print(hex(10))
print(type(hex(10)))
h = 0b1010
print(h)
print(type(h))
