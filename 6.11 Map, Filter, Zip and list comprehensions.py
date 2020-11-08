l = [1, 2, 3]


def sq(x):
    return x ** 2


print(list(map(sq, l)))

l1 = [1, 2, 3]
l2 = [10, 20, 30]


def add(x, y):
    return x + y


print(list(map(add, l1, l2)))
print(list(map(lambda x, y: x + y, l1, l2)))

l = [0, 1, 2, 3]
print(list(filter(None, l)))


def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, l)))
print(list(zip(l1, l2)))
# stop at shorter one length in case of not equal

l = range(100)
s = 'abcd'
print(list(zip(l, s)))

print([x + y for x, y in zip(l1, l2)])

print([x+1 for x in l2 if x %2 == 0])

l = range(10)
print(list(filter(lambda y: y<25, map(lambda x: x**2, l))))
print([x**2 for x in l if x**2 < 25])

