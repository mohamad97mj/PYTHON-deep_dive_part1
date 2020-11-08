import sys
import ctypes

a = [1, 2, 3]
b = a
print(sys.getrefcount(a))


def ref_count(address):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(a)))
