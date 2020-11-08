class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # implementing theses method adds login with not breaking backward compatibility
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError('width must be positive')
        else:
            self._width = width

    def area(self):
        return self.width * self.height

    def __str__(self):
        # this will execute when call str on object or when printing it
        return "Rectangle with width:{} and height:{}".format(self.width, self.height)

    def __repr__(self):
        return "this will execute just in console mode"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.area() < other.area()


r1 = Rectangle(5, 10)
r2 = Rectangle(5, 10)
r3 = 10
r4 = Rectangle(20, 30)
print(r1 == r2)
print(r1 == r3)
print(r1 < r4)
print(r4 > r1)
# print(r1 <= r4)
print(r1.width)
# print(r1.height)
r1.test = 100
print(r1.test)
r6 = Rectangle(10, 6)
r6.width = -10
r7 = Rectangle(-5, 5)

