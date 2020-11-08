a = [1, 2]
b = [4, 5]

c = (a, b)
print(c)
a.append(3)
b.append(6)
print(c)

#  tuples are immutable but they can contain mutable objects

a = [1, 2, 3]
print(hex(id(a)))
a.append(5)
print(hex(id(a)))
a = a + [5]
print(hex(id(a)))

t = (1, 2, 3)
print(hex(id(t[0])))
print(hex(id(t[1])))
print(hex(id(t[2])))

b = 2
print(hex(id(b)))
