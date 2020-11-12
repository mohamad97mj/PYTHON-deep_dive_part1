from fractions import Fraction


def dec_speak(cls):
    cls.speak = lambda self, message: "{0} says : {1}".format(cls.__class__.__name__, message)
    return cls


Fraction = dec_speak(Fraction)

f = Fraction()
print(f.speak("i am just created"))


@dec_speak
class Person:
    pass


p = Person()
print(p.speak("hello there"))
