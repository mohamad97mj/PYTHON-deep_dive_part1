print(callable(print))
print(callable(int))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(10))


class A:
    def __init__(self):
        self.counter = 0


print(callable(A))

a = A()
print(callable(a))


class B:
    def __init__(self):
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 10


b = B()
print(callable(b))
b()
print(b.counter)