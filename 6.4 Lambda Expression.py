def apply_func(x, fn):
    return fn(x)


print(apply_func(3, lambda x: x ** 3))


# the body of lambda is limited to a single expression
# no assignment
# no annotation


