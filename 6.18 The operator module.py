import operator
from functools import reduce

print(operator.add(1, 2))
print(operator.mul(3, 2))
print(operator.truediv(3, 2))
print(operator.floordiv(3, 2))

print(reduce(lambda x, y: x * y, [1, 2, 3]))
print(reduce(operator.mul, [1, 2, 3]))

print(operator.lt(10, 3))
print(operator.truth([]))
my_list = [1, 2, 3]
print(operator.getitem(my_list, 1))

f = operator.itemgetter(2)
print(f(my_list))
f = operator.itemgetter(2, 1)
print(f(my_list))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self, d=10):
        print("test method running")
        print(d)


my_obj = MyClass()

prop_a = operator.attrgetter('a')
print(prop_a(my_obj))

my_var = 'b'
prop_b = operator.attrgetter(my_var)
print(prop_b(my_obj))

a, b, test = operator.attrgetter('a', 'b', 'test')(my_obj)
print(a, b, test)

test()

f = lambda x: x.a
print(f(my_obj))

l = [5 - 10j, 3 + 3j, 2 - 100j]
print(sorted(l, key=operator.attrgetter('real')))
print(sorted(l, key=lambda x: x.real))
f = operator.methodcaller('test')
f(my_obj)
operator.methodcaller('test', 10)(my_obj)