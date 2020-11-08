import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


print(time_it(print, 1, 2, 3, rep=5, sep='-', end='***\n'))
