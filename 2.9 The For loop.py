# iterable = 'abcd'
# iterable = ('a', 'b', 'c')
iterable = [('a', 1), ('b', 2), ('c', 3)]

for x, y in iterable:
    print(x, y)


s = 'abcd'
for i, c in enumerate(s):
    print(i, c)


for i in range(5):
    print('------------')
    try:
        10 / (3 - i)
    except ZeroDivisionError:
        print('division by zero')
        continue
    finally:
        print('always run')
    print(i)