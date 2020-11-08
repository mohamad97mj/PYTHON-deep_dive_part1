from typing import List


def process(s):
    print("initial address: ", hex(id(s)))
    s = s + 'world'
    print("final address: ", hex(id(s)))


my_var = 'hello'
print(hex(id(my_var)))
process(my_var)
print(hex(id(my_var)))
print(my_var)

my_list = [1, 2, 3]


def modify_list(lst: List):
    print("initial lst address: ", hex(id(lst)))
    lst.append(4)
    print("final lst address: ", hex(id(lst)))


print(hex(id(my_list)))
modify_list(my_list)
print(hex(id(my_list)))
print(my_list)
