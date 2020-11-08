def func(a: int, b: int):  # this is just for doc
    return a * b


print(func('test', 3))
print(func)


def func1():
    return func2()


def func2():
    return "func2 is running"


func1()


def func3():
    return func4()


# func3() this will cause error


def func4():
    return "func4 is running"


func5 = func4
print(func5())

func6 = lambda x: x * 2  # not recommended, do not assign a lambda expression
print(func6(3))
