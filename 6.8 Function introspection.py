import inspect
import math


def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass


print(my_func.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)


class MyClass:
    def func(self):
        pass


my_obj = MyClass()
print(inspect.isfunction(my_func))
print(inspect.isfunction(my_obj.func))
print(inspect.ismethod(my_obj.func))
print(inspect.getsource(my_func))
print(inspect.getmodule(my_func))
print(inspect.getmodule(print))
print(math.sin)

s = inspect.signature(my_func)

for param in s.parameters.values():
    print(param.name)
    print(param.kind)
    print(param.annotation)
    print(param.default)

print(dir(my_func))
# returns valid attribute
