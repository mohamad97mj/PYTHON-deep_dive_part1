a = 10
print(hex(id(a)))
print(type(a))
a = 15
print(hex(id(a)))
a = a + 1
print(hex(id(a)))
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
# integers are immutable
