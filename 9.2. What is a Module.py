import math
import fractions
import sys
import types


def my_func():
    a = 10
    return a


print(globals())
print(globals()['my_func']())

print(locals() is globals())


def test():
    a = 10
    print(locals() is globals())
    print(locals())


test()
print(math)
print(fractions)

print(id(math))
print(type(math))
import math

print(id(math))
junk = math

print(globals())
print(type(sys.modules))
print(sys.modules['math'])
print(id(sys.modules['math']))

f = globals()['math'].__dict__['sqrt']
print(f(9))

print(dir(fractions))
# print(fractions.__dict__)

print(isinstance(fractions, types.ModuleType))
print(type(type))
# print(type(types.ModuleType))
mod = types.ModuleType('test', 'This is a test Module')
print(isinstance(mod, types.ModuleType))

print(mod.__dict__)
mod.pi = 3.14
mod.hello = lambda : "hello"
print(mod.hello())

print('mod' in globals())