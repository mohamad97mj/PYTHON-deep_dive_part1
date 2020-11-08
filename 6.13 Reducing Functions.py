import functools
from functools import reduce


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


l = [1, 2, 3, 8, 4, 5, 10]
print(_reduce(lambda x, y: x if x > y else y, l))
print(_reduce(lambda x, y: x if x < y else y, l))
print(_reduce(lambda x, y: x + y, l))
print(reduce(lambda x, y: x if x > y else y, l))
print(reduce(lambda x, y: x if x < y else y, l))
print(reduce(lambda x, y: x + y, l))

# print(_reduce(lambda x, y: x if x > y else y, {2, 10, 3, 5}))
print(reduce(lambda x, y: x if x > y else y, {2, 10, 3, 5}))

print(min(l))
print(max(l))
print(sum(l))
print(any(l))
print(all(l))

print(_reduce(lambda x, y: bool(x) or bool(y), l))
print(_reduce(lambda x, y: bool(x) and bool(y), l))
print(_reduce(lambda x, y: x * y, range(1, 5 + 1)))
# this is factorial

l = []
# print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: x + y, l, 1))
l = [1, 2, 3]
print(reduce(lambda x, y: x + y, l, 100))
print(reduce(lambda x, y: x + y, l, 0))
print(reduce(lambda x, y: x * y, l, 1))
