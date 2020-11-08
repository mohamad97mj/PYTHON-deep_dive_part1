# circular references
import ctypes
import gc


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_bY_ic(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, B: {1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, A: {1}'.format(hex(id(self)), hex(id(self.a))))


gc.disable()

my_var = A()

a_id = id(my_var)
b_id = id(my_var.b)

print(ref_count(a_id))
print(ref_count(b_id))
print(object_bY_ic(a_id))
my_var = None
print(ref_count(a_id))
print(ref_count(b_id))
print(object_bY_ic(a_id))
print(object_bY_ic(b_id))
gc.collect()
print(object_bY_ic(a_id))
print(ref_count(a_id))
print(ref_count(b_id))
