import string
import time

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 10000
    e = 'the quick brown fox'
    f = ['a', 'b'] * 3
    x = 2
    if x in [1, 2, 3]:
        print(x)

    y = 3
    if y in {1, 2, 3}:
        print(y)


print(my_func.__code__.co_consts)
print(string.ascii_letters)
char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list:', end - start)


start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple:', end - start)


start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set:', end - start)

