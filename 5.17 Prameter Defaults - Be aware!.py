from datetime import datetime


def log(msg, *, dt=datetime.utcnow()):
    print(msg, dt)


log('message1')
log('message2')
log('message3')


# so we should not do that instead:

def log2(msg, dt=None):
    dt = dt or datetime.utcnow()
    print(msg, dt)


log2('message1')
log2('message2')
log2('message3')


def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list


store1 = add_item("item1")
store2 = add_item("item2")

print(store1)
print(store2)

print(store1 is store2)


# never use mutable in default values because they once evaluate at the definition time instead:


def add_item2(item, my_list=None):
    my_list = my_list or []
    my_list.append(item)
    return my_list


store1 = add_item2("item1")
store2 = add_item2("item2")

print(store1)
print(store2)
