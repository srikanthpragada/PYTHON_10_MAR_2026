import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, l, w):
        super().__init__(x, y)
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
