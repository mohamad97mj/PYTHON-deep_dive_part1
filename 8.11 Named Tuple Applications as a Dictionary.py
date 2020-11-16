from collections import namedtuple

data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 2, 'key2': 3},
    {'key1': 1, 'key2': 2, 'key3': 3},
    {'key2': 1},
]

keys = {key for dic_ in data_list for key in dic_.keys()}
print(keys)

Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)
Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
s = Struct(key3=10)
print(s)
tuple_list = [Struct(**_) for _ in data_list]
print(tuple_list)


def tuplify_dicts(dicts):
    keys = {key for dic_ in dicts for key in dic_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**_) for _ in data_list]


print(tuplify_dicts(data_list))
