def timed(reps):
    def dec(fn):
        from functools import wraps
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_time = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_time += end - start
            average_time = total_time / reps

            print("{0} ran for average of {1:.6f}s".format(fn.__name__, average_time))
            return result

        return inner

    return dec


class MyTime:
    def __init__(self, reps):
        self.reps = reps

    def __call__(self, fn):
        from functools import wraps
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_time = 0
            for i in range(self.reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_time += end - start
            average_time = total_time / self.reps

            print("{0} ran for average of {1:.6f}s".format(fn.__name__, average_time))
            return result
        return inner


# @timed(10)
@MyTime(10)
def fact(n):
    from operator import mul
    from functools import reduce
    return reduce(mul, range(1, n + 1))


fact(10)
fact(1000)
