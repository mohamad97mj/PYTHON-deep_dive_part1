import string

# not --> and --> or
print(True or True and False)

# True or Y -> True
# False and Y -> False

a = 10
b = 0

if b and a / b > 2:
    print('a is at least twice b')

if name and name[0] in string.digits:
    print("name can not start with a digit")

# this is equal to
if (name is not None and len(name) > 0) and name[0] in string.digits:
    print("name can not start with a digit")


