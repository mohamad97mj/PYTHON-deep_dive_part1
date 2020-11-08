# == equality operator for object state(data)
# is identity operator for memory address

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

a = 10
b = 10.0
print(a == b)


a = None
b = None
c = None
print(id(a))
print(id(b))
print(id(c))
print(type(None))
a = 10
b = 10.0
c = 10 + 0j
print(a == c)
print(a is c)
