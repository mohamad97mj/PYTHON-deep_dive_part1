a = int()
print(a)
b = int('101', base=2)
print(b)
c = 5
print(id(b))
print(id(c))


def square(a):
    return a ** 2


print(type(square))
f = square

print(f(8))
print(id(f))
print(id(square))
print(f is square)


def cube(a):
    return a ** 3


def select_function(fun_id):
    if fun_id == 1:
        return square
    else:
        return cube


g = select_function(2)
print(g(9))
print(g is square)
print(select_function(1)(6))


def exec_function(fn, n):
    return fn(n)


print(exec_function(cube, 6))
