def put_it_together(a, b, c=10, *args, d, e=7, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(d)
    print(e)
    print(kwargs)
    print('.......')


put_it_together(10, 20, 30, 40, 50, d=7)
put_it_together(10, 20, d=5)
put_it_together(b=10, a=20, d=5, g=8, h=9)


def put_it_together2(a, b=10, *args, d, e=7, **kwargs):
    print(a)
    print(b)
    print(args)
    print(d)
    print(e)
    print(kwargs)
    print('.......')


# put_it_together2(1, 'x', 'y', 'z', b=2, d=3)
# got multiple values for argument 'b'
