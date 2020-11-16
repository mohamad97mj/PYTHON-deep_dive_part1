from random import randint, random
from collections import namedtuple

Color = namedtuple('Color', 'red green blue alpha')


def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = randint(0, 1)
    return Color(red, blue, green, alpha)


color = random_color()
print(color)


key = 'red'
print(getattr(color, key))
