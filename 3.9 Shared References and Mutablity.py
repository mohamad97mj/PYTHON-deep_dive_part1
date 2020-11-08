a = 'hello'
b = a
c = 'hello'
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))
# for optimization
# it is safe to do
b = 'hello world'
print(hex(id(b)))
print(hex(id(a)))

a = [1, 2, 3]
b = a
print(hex(id(a)))
print(hex(id(b)))
b.append(4)
print(a)
print(hex(id(a)))
print(hex(id(b)))

c = [1, 2, 3]
d = [1, 2, 3]
print(hex(id(c)))
print(hex(id(d)))


a = 500000000
b = 50000000
print(id(a))
print(id(b))

