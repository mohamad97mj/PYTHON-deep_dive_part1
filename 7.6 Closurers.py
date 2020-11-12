def outer():
    x = "mohammad"
    y = 10
    print(hex(id(x)))
    print(hex(id(y)))

    def inner():
        y = 100
        print("hello {}".format(x))
        print(hex(id(x)))
        print(hex(id(y)))

    return inner


f = outer()
f()

print(f.__code__.co_freevars)
print(f.__closure__)


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


f = counter()
f2 = counter()
print(f())
print(f())
print(f())
print(f2())


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc, inc2


f1, f2 = counter()
print(f1())
print(f1())
print(f1())
print(f2())

# for i in range(6):
#     print(i)
#
# print(i)

adders = []
for n in range(1, 4):
    adders.append(lambda x: x + 5)
print(adders[0](10))

