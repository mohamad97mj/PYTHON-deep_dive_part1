from collections import namedtuple


point2d = namedtuple('Point2d', 'x y')
# point2d = namedtuple('Point2d', 'x _y')
p = point2d(10, 20)
print(p[0])
print(p.x)
print(p.y)

for e in p:
    print(e)

p2 = point2d(x=5, y=6)

# class Point2d(tuple):
# p2.x = 100

print(p2._fields)
print(point2d._fields)
# print(point2d._source)
print(p2._asdict())

# p2._make()
# p2._replace()
# new_fields = p2._fields + ('new_field', )
