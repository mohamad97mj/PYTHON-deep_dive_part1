def func(a, b, *c):  # better to use *args
    print(a, b, c)
    print(type(c))


func(1, 2, 3, 4, 5)


# for using mandatory keywords arguments
def func2(a, b, *args, d):
    print(a, b, args, d)


# func2(1, 2, 3, 4, 5)
func2(1, 2, 3, 4, d=5)
func2(1, 2, d=5)
# func2(1, 2)

l = [10, 20, 30]


def func3(a, b, c):
    print(a, b, c)


func3(*l)


def func4(*args, d):
    print(args, d)


func4(1, 2, 3, d=4)
func4(d=4)


def func5(*, d):
    print(d)


func5(d=5)


# func5(1, 2, d=5)


def func6(a, b=1, *args, d, e=True):
    print('b is:', b)
    print(a, b, args, d, e)


func6(1, 2, 3, d=4, e=5)
func6(1, d=5)


# it seems we can not specify args without specify b


def func7(a, b, *, d):
    print(a, b, d)


func7(1, 2, d=3)


# func7(1, 2, 3, d=4)

def func8(a, b=1, *args, d=0, e):
    print('b is:', b)
    print(a, b, args, d, e)


func8(1, *(10, 2, 3), e=9)
