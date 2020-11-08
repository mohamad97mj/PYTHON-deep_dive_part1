import sys

a = 'dsfdsfadffgffgtgh df, 12'
b = 'dsfdsfadffgffgtgh df, 12'
print(hex(id(a)))
print(hex(id(b)))

d = sys.intern("hello, world")
e = sys.intern("hello, world")

print(hex(id(d)))
print(hex(id(e)))