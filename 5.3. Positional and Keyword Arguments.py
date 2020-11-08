# def f(a, b, c):
#     print(a, b, c)
#
#
# f(1, 2, b=3)
#
#
# def f2(a, b=3, c):
#     print(a, b, c)
#
#
# f2(1, 2, 3)
#
#
# def f3(a, b, c):
#     print(a, b, c)
#
#
# f3(a, b=2, c)


def test(a, b, /, c):
    return a * b + c


# print(test(a=2, b=3, c=4))
print(test(2, 3, c=4))
