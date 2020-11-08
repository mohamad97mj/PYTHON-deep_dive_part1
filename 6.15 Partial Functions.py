from functools import partial

def my_func(a, b, c):
    print(a, b, c)


def fn(b, c):
    return my_func(10, b, c)


fn(20, 30)

f = lambda b, c: my_func(10, b, c)
f(20, 30)

f = partial(my_func, 10)
f(20, 30)


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, *args, k1, k2, **kwargs)


def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)


f = partial(my_func, 10, k1='a')


square = partial(pow, exp=2)
print(square(5))
cube = partial(pow, exp=3)
print(cube(5))
print(square(5, exp=4))

