# x or y  if x is truthy returns x otherwise returns y
# x and y if x is falsy return x otherwise return y

x = None
y = 'hello'
print(x or y)
print(x and y)
print(y and x)
print(y or x)

a = 0
a = a or 1
print(a)
# this is equal to :
a = 0
if a == 0:
    a = 1
print(a)

a = 5
a = a and 10 / a
print(a)

# this is equal to :
a = 5
if a != 0:
    a = 10 / a

print(a)

s = 'hello'
if s:
    b = s[0]
else:
    b = ''


# this is equal to:

b = (s and s[0]) or ''

