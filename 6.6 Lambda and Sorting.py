import random

l = [1, 2, 8, 6, 4, 9]
print(sorted(l))
print(l)
# not inplace sorting


l = ['a', 'B', 'd', 'C']
print(sorted(l))
print(ord('a'))
print(ord('B'))

print(sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(sorted(d))
print(sorted(d, key=lambda e: d[e]))


def dist_sq(x):
    return (x.real) ** 2 + (x.imag) ** 2


print(dist_sq((2 + 3j)))

l = [0j, 1 - 1j, 3 + 0j, 3 + 3j]
# print(sorted(l))
print(sorted(l, key=dist_sq))
print(sorted(l, key=lambda x: x.real ** 2 + x.imag ** 2))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sorted(l, key=(lambda: random.random())))
print(sorted(l, key=(lambda x: random.random())))

get_5 = lambda: random.random()

print(get_5())  # 5
