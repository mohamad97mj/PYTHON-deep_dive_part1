def func(a, b, *, d, **kwargs):
    print(a, b, d, kwargs)


func(10, 20, d=30, y=60, x=50)

# def f(a, b, *):
#     print(a, b,)

