def my_func():
    """ this is a function that return  0 to test docstrings for functions help"""
    return 0


print(help(my_func))


def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    """ this is a function that return concatenation of a function with itself b times"""
    return a * b


print(help(my_func))


def my_func(a: str, b: 'int > 0') -> str:
    """ this is a function that return concatenation of a function with itself b times"""
    return a * b


print(help(my_func))

print(my_func.__annotations__)