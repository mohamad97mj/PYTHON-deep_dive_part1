
print(bool(-1))
print(bool(0))
print(bool(100))
print(bool(None))
print(bool(list()))
print(bool(list([1])))

x = 2
print(bool(x) == x.__bool__())
print((100).__bool__())
x = ''
print(bool(x))
print(bool(x.__len__()))

a = [1, 2, 3]
if a:
    pass

if a is not None and len(a) > 0:
    pass

