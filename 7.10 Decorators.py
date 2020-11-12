from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('function {0} has called {1} times'.format(fn.__name__, count))
        # inner.__name__ = fn.__name__
        # inner.__doc__ = fn.__doc__
        return fn(*args, **kwargs)

    # inner = wraps(fn)(inner)
    return inner


@counter
def add(a, b=0):
    return a + b


# add = counter(add)
print(add(2, 5))
print(add(3, 7))
print(add.__name__)
