a, *b = [-10, 5, 2, 100]
print(a, b)

a, *b = (-10, 5, 2, 100)
print(a, b)
print(type(b))

a, *b = 'XYZ'
print(a, b)
print(type(b))

a, b, *c = 1, 2, 3, 4, 5
print(a, b, c)

a, b, *c, d = [1, 2, 3, 4, 5]
print(a, b, c, d)

a, *b, c, d = 'python'
print(a, b, c, d)

# wrong
# a, *b, c, *d = [1, 2, 3, 4, 5, 6]

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]
print(l3)

s = {10, 99, -11, 'd'}
print(s)

a, *b, c = s
print(a, b, c)
# not count on answer

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}
d = {*d1, *d2, *d3}
print(d)
d = [*d1, *d2, *d3]
print(d)

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}
# for repeated keys it uses the last value, here 'h'
d = {**d1, **d2, **d3}
print(d)

#  **  can not be uses in LHS

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'c': 3, **d1}
print(d2)

l = [1, 2, [3, 4]]
a, b, c = l
print(a, b, c)
a, b, (c, d) = l
print(a, b, c, d)

a, *b, (c, d, e) = [1, 2, 3, 'xyz']
print(a, b, c, d, e)

a, *b, (c, *d) = [1, 2, 3, 'xyz']
print(a, b, c, d, e)
