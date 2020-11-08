a = [1, 2, 3]
a = [1, 2,
     3, 4]
a = [1  # item1
    , 20]
a = [1,  # item1
     2]


def my_func(a,  # comment
            b,  # comment
            c  # comment
            ):
    print(a, b, c)


my_func(10,  # comment
        20,  # comment
        30  # comment
        )

a = 10
b = 20
c = 30

if a > 5 \
        and b > 10 \
        and c > 20:
    print("hello world!")

a = '''this is a string'''
print(a)

a = '''this
is a string'''
print(a)

a = '''this
    is a string
       that is created over multiple line'''
print(a)

a = '''some items:
       1.item1
       2.item2'''
print(a)


def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a


print(my_func())
