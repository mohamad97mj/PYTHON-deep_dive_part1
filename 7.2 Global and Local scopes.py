# print = lambda x: 'hello {0}'.format(x)
# s = print('world')
#
# def test():
#     dsfj;
#     a;
#     dsfj
#     asdf
#     a = a + 1


a = 10


# def test2():
#     a = a + 3
#     print(a)

# test2()


def test3():
    global a
    a = a + 3
    global b
    b = 5
    print(a)
    print(b)


test3()


# because in compile time a is assigned to 100 amd then it is not counted as global variable
def test4():
    print(a)
    a = 100


test4()


