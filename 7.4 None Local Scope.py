b = 5
w = 'here'
h = 100


def outer_func():
    a = 10
    x = 'hello'
    y = 'hello2'
    e = 3
    h = 'i am h'

    def inner_func():
        global c
        nonlocal y, h
        # nonlocal w
        # nonlocal z
        h = 'i am h in inner'
        c = 1000
        print(a)
        print(b)
        x = 'goodbye'
        y = 'goodbye2'

        # print(z)
        # print(w)
        def inner2_func():
            global h
            h = 5
            nonlocal e
            e = 5

        inner2_func()

    inner_func()
    print(h)
    print(x)
    print(y)
    print(e)


outer_func()
print(c)
print(h)
